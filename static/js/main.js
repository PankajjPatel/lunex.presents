/**
 * Lunex Presents — Main JavaScript
 * Handles: navbar scroll, portfolio filters, scroll reveal, form UX
 */

'use strict';

/* ─── 0. THEME CONTROLLER ─────────────────────────────── */
// Theme switching is handled cleanly by window.toggleLunexTheme in base.html


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

/* ─── 8. INTERACTIVE PROJECT GALLERY ──────────────────── */
(function () {
  const mainImg = document.querySelector('#gallery-main-img');
  const mainCaption = document.querySelector('#gallery-main-caption');
  const thumbs = document.querySelectorAll('.gallery-thumb-item');
  if (!mainImg || !thumbs.length) return;

  let currentIndex = 0;
  const items = Array.from(thumbs).map(t => ({
    src: t.getAttribute('data-full-src'),
    caption: t.getAttribute('data-caption') || '',
    index: parseInt(t.getAttribute('data-index') || '0', 10),
  }));

  const activateImage = (idx) => {
    if (idx < 0 || idx >= items.length) return;
    currentIndex = idx;
    const item = items[idx];

    // Smooth transition
    mainImg.style.transition = 'opacity 0.2s ease, transform 0.2s ease';
    mainImg.style.opacity = '0.3';
    mainImg.style.transform = 'scale(0.99)';

    setTimeout(() => {
      mainImg.src = item.src;
      if (mainCaption) mainCaption.textContent = item.caption;
      mainImg.style.opacity = '1';
      mainImg.style.transform = 'scale(1)';
    }, 180);

    thumbs.forEach((th, i) => {
      if (i === idx) {
        th.classList.add('active');
        th.setAttribute('aria-selected', 'true');
      } else {
        th.classList.remove('active');
        th.setAttribute('aria-selected', 'false');
      }
    });
  };

  thumbs.forEach((thumb, i) => {
    thumb.addEventListener('click', () => activateImage(i));
  });

  const prevBtn = document.querySelector('#gallery-prev');
  const nextBtn = document.querySelector('#gallery-next');

  if (prevBtn) {
    prevBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const prevIdx = (currentIndex - 1 + items.length) % items.length;
      activateImage(prevIdx);
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const nextIdx = (currentIndex + 1) % items.length;
      activateImage(nextIdx);
    });
  }

  // Lightbox modal preview
  const modalImg = document.querySelector('#lightbox-modal-img');
  const modalCaption = document.querySelector('#lightbox-modal-caption');
  const expandBtns = document.querySelectorAll('[data-gallery-lightbox]');
  expandBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const src = btn.getAttribute('data-img-src') || mainImg.src;
      const cap = btn.getAttribute('data-img-caption') || (mainCaption ? mainCaption.textContent : '');
      if (modalImg) modalImg.src = src;
      if (modalCaption) modalCaption.textContent = cap;
    });
  });
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
