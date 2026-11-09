from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.utils.text import slugify

from contact.models import Enquiry, Review
from portfolio.models import Project, Category
from services.models import Service
from audit.models import AuditScan
from .forms import DashboardLoginForm, ProjectForm


def staff_required(view_func):
    """Decorator ensuring user is authenticated and staff/superuser."""
    return user_passes_test(
        lambda u: u.is_authenticated and u.is_staff,
        login_url='/dashboard/login/'
    )(view_func)


def dashboard_login(request):
    """
    Locked Admin Portal Login.
    Public registration is strictly disabled.
    Only pre-configured administrator accounts can log in.
    """
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('dashboard:home')

    if request.method == 'POST':
        form = DashboardLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                next_url = request.GET.get('next') or 'dashboard:home'
                return redirect(next_url)
            else:
                messages.error(request, "Access denied. Administrator privileges required.")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = DashboardLoginForm()

    context = {
        'form': form,
        'page_title': 'Admin Portal Login — Lunex Presents',
        'meta_description': 'Restricted access administrator portal for Lunex Presents.',
    }
    return render(request, 'dashboard/login.html', context)


@staff_required
def dashboard_logout(request):
    """Log out of the administrator dashboard."""
    logout(request)
    messages.info(request, "You have been logged out of the administrator portal.")
    return redirect('core:home')


@staff_required
def dashboard_home(request):
    """Central Administrator Overview."""
    total_enquiries = Enquiry.objects.count()
    unread_enquiries = Enquiry.objects.filter(is_read=False).count()
    recent_enquiries = Enquiry.objects.all()[:6]

    total_reviews = Review.objects.count()
    pending_reviews = Review.objects.filter(is_approved=False).count()
    recent_reviews = Review.objects.all()[:4]

    total_projects = Project.objects.count()
    total_services = Service.objects.count()
    total_audits = AuditScan.objects.count()

    context = {
        'page_title': 'Admin Overview — Lunex Presents',
        'total_enquiries': total_enquiries,
        'unread_enquiries': unread_enquiries,
        'recent_enquiries': recent_enquiries,
        'total_reviews': total_reviews,
        'pending_reviews': pending_reviews,
        'recent_reviews': recent_reviews,
        'total_projects': total_projects,
        'total_services': total_services,
        'total_audits': total_audits,
    }
    return render(request, 'dashboard/home.html', context)


# ─────────────────────────────────────────────────────────────
# Enquiries Management
# ─────────────────────────────────────────────────────────────

@staff_required
def enquiries_list(request):
    """View and filter customer enquiries."""
    enquiry_filter = request.GET.get('type', 'all')
    status_filter = request.GET.get('status', 'all')

    enquiries = Enquiry.objects.all()

    if enquiry_filter != 'all':
        enquiries = enquiries.filter(enquiry_type=enquiry_filter)
    if status_filter == 'unread':
        enquiries = enquiries.filter(is_read=False)
    elif status_filter == 'read':
        enquiries = enquiries.filter(is_read=True)

    unread_count = Enquiry.objects.filter(is_read=False).count()

    context = {
        'page_title': 'Customer Enquiries — Lunex Dashboard',
        'enquiries': enquiries,
        'unread_count': unread_count,
        'current_type': enquiry_filter,
        'current_status': status_filter,
    }
    return render(request, 'dashboard/enquiries.html', context)


@staff_required
def enquiry_detail(request, pk):
    """Detailed view of an individual enquiry."""
    enquiry = get_object_or_404(Enquiry, pk=pk)
    if not enquiry.is_read:
        enquiry.is_read = True
        enquiry.save(update_fields=['is_read'])

    context = {
        'page_title': f'Enquiry from {enquiry.name} — Lunex Dashboard',
        'enquiry': enquiry,
    }
    return render(request, 'dashboard/enquiry_detail.html', context)


@staff_required
@require_POST
def enquiry_mark_read(request, pk):
    """Toggle read status of an enquiry."""
    enquiry = get_object_or_404(Enquiry, pk=pk)
    enquiry.is_read = not enquiry.is_read
    enquiry.save(update_fields=['is_read'])
    status_label = "read" if enquiry.is_read else "unread"
    messages.success(request, f"Marked enquiry #{enquiry.id} as {status_label}.")
    return redirect(request.META.get('HTTP_REFERER') or 'dashboard:enquiries')


# ─────────────────────────────────────────────────────────────
# Reviews Moderation
# ─────────────────────────────────────────────────────────────

@staff_required
def reviews_list(request):
    """Moderation queue for client reviews."""
    filter_val = request.GET.get('filter', 'all')
    reviews = Review.objects.all()

    if filter_val == 'pending':
        reviews = reviews.filter(is_approved=False)
    elif filter_val == 'approved':
        reviews = reviews.filter(is_approved=True)

    pending_count = Review.objects.filter(is_approved=False).count()

    context = {
        'page_title': 'Reviews Moderation — Lunex Dashboard',
        'reviews': reviews,
        'pending_count': pending_count,
        'current_filter': filter_val,
    }
    return render(request, 'dashboard/reviews.html', context)


@staff_required
@require_POST
def review_toggle_approve(request, pk):
    """Approve or reject a review."""
    review = get_object_or_404(Review, pk=pk)
    review.is_approved = not review.is_approved
    review.save(update_fields=['is_approved'])
    action = "approved and published" if review.is_approved else "hidden from public view"
    messages.success(request, f"Review by '{review.client_name}' has been {action}.")
    return redirect('dashboard:reviews')


@staff_required
@require_POST
def review_toggle_verify(request, pk):
    """Toggle verified client badge."""
    review = get_object_or_404(Review, pk=pk)
    review.is_verified_client = not review.is_verified_client
    review.save(update_fields=['is_verified_client'])
    badge = "marked as Verified Client" if review.is_verified_client else "unmarked as verified"
    messages.success(request, f"Review by '{review.client_name}' {badge}.")
    return redirect('dashboard:reviews')


@staff_required
@require_POST
def review_delete(request, pk):
    """Delete a review."""
    review = get_object_or_404(Review, pk=pk)
    client_name = review.client_name
    review.delete()
    messages.warning(request, f"Review by '{client_name}' has been permanently deleted.")
    return redirect('dashboard:reviews')


# ─────────────────────────────────────────────────────────────
# Portfolio Management
# ─────────────────────────────────────────────────────────────

@staff_required
def portfolio_list(request):
    """Manage portfolio projects."""
    projects = Project.objects.all().select_related('category').prefetch_related('images')
    context = {
        'page_title': 'Portfolio Management — Lunex Dashboard',
        'projects': projects,
    }
    return render(request, 'dashboard/portfolio.html', context)


@staff_required
def portfolio_add(request):
    """Add a new portfolio project."""
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            if not project.slug:
                project.slug = slugify(project.title)
            project.save()
            messages.success(request, f"Project '{project.title}' added successfully!")
            return redirect('dashboard:portfolio')
    else:
        form = ProjectForm()

    context = {
        'page_title': 'Add Project — Lunex Dashboard',
        'form': form,
        'action': 'Add',
    }
    return render(request, 'dashboard/portfolio_form.html', context)


@staff_required
def portfolio_edit(request, pk):
    """Edit an existing portfolio project."""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, f"Project '{project.title}' updated successfully!")
            return redirect('dashboard:portfolio')
    else:
        form = ProjectForm(instance=project)

    context = {
        'page_title': f'Edit {project.title} — Lunex Dashboard',
        'form': form,
        'project': project,
        'action': 'Edit',
    }
    return render(request, 'dashboard/portfolio_form.html', context)


@staff_required
@require_POST
def portfolio_delete(request, pk):
    """Delete a portfolio project."""
    project = get_object_or_404(Project, pk=pk)
    title = project.title
    project.delete()
    messages.warning(request, f"Project '{title}' has been deleted.")
    return redirect('dashboard:portfolio')


# ─────────────────────────────────────────────────────────────
# Services Overview
# ─────────────────────────────────────────────────────────────

@staff_required
def services_list(request):
    """View services and pricing."""
    services = Service.objects.all()
    context = {
        'page_title': 'Services Overview — Lunex Dashboard',
        'services': services,
    }
    return render(request, 'dashboard/services.html', context)
