/**
 * Lunex Presents — Main JavaScript
 * Handles: navbar scroll, portfolio filters, scroll reveal, form UX
 */

'use strict';

/* ─── 1. NAVBAR SCROLL EFFECT ─────────────────────────── */
(function () {
  const navbar = document.querySelector('.lx-navbar');
  if (!navbar) return;

  const onScroll = () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll(); // Run on load
})();

/* ─── 2. ACTIVE NAV LINK ──────────────────────────────── */
(function () {
  const currentPath = window.location.pathname;
  document.querySelectorAll('.lx-navbar .nav-link').forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    if (
      (href === '/' && currentPath === '/') ||
      (href !== '/' && currentPath.startsWith(href))
    ) {
      link.classList.add('active');
    }
  });
})();

/* ─── 3. PORTFOLIO FILTERS ────────────────────────────── */
(function () {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const items = document.querySelectorAll('.portfolio-item');
  if (!filterBtns.length || !items.length) return;

  const portfolioGrid = document.querySelector('#portfolio-grid');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.dataset.filter;

      // Update active button
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Show/hide items with animation
      let visibleCount = 0;
      items.forEach(item => {
        const cat = item.dataset.category;
        const show = filter === 'all' || cat === filter;
        if (show) {
          item.classList.remove('hidden');
          item.style.position = '';
          item.style.visibility = '';
          visibleCount++;
        } else {
          item.classList.add('hidden');
        }
      });

      // Show empty state if no results
      const emptyState = document.querySelector('#portfolio-empty');
      if (emptyState) {
        emptyState.style.display = visibleCount === 0 ? 'block' : 'none';
      }
    });
  });
})();

/* ─── 4. SCROLL REVEAL ────────────────────────────────── */
(function () {
  const revealEls = document.querySelectorAll('.reveal');
  if (!revealEls.length) return;

  // Respect reduced-motion
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) {
    revealEls.forEach(el => el.classList.add('revealed'));
    return;
  }

  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
  );

  revealEls.forEach(el => observer.observe(el));
})();

/* ─── 5. CONTACT FORM UX ──────────────────────────────── */
(function () {
  const form = document.querySelector('#contact-form');
  if (!form) return;

  const submitBtn = form.querySelector('[type="submit"]');
  if (!submitBtn) return;

  form.addEventListener('submit', () => {
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Sending...';
  });
})();

/* ─── 6. AUTO-DISMISS ALERTS ──────────────────────────── */
(function () {
  document.querySelectorAll('.alert[data-auto-dismiss]').forEach(alert => {
    const delay = parseInt(alert.dataset.autoDismiss, 10) || 5000;
    setTimeout(() => {
      alert.style.transition = 'opacity 0.5s ease';
      alert.style.opacity = '0';
      setTimeout(() => alert.remove(), 500);
    }, delay);
  });
})();

/* ─── 7. SMOOTH SCROLL FOR ANCHOR LINKS ──────────────── */
(function () {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
})();
