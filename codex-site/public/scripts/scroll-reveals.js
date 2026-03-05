// ═══════════ SCROLL REVEAL SYSTEM ═══════════
// Phase 5C — Intersection Observer for fade-in reveals, staggered entrances, scroll-spy

function initScrollReveals() {

  // Respect user preference for reduced motion
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('.scroll-reveal').forEach(el => {
      el.classList.add('revealed');
    });
    document.querySelectorAll('.stagger-child').forEach(el => {
      el.classList.add('revealed');
    });
    return;
  }

  // Single elements — fade up on enter
  // Use threshold 0 with rootMargin to handle tall content cards
  // (a 12% threshold on a 5000px card requires 600px visible — often more than viewport)
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        revealObserver.unobserve(entry.target); // Only reveal once
      }
    });
  }, {
    threshold: 0,
    rootMargin: '0px 0px -40px 0px'
  });

  document.querySelectorAll('.scroll-reveal').forEach(el => {
    revealObserver.observe(el);
  });

  // Staggered groups — children reveal in sequence
  const staggerObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const children = entry.target.querySelectorAll('.stagger-child');
        children.forEach((child, i) => {
          child.style.transitionDelay = `${i * 80}ms`;
          child.classList.add('revealed');
        });
        staggerObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.08,
    rootMargin: '0px 0px -40px 0px'
  });

  document.querySelectorAll('.stagger-group').forEach(el => {
    staggerObserver.observe(el);
  });

  // ═══════════ SCROLL-SPY FOR SIDEBAR ═══════════
  const sections = document.querySelectorAll('[data-spy-section]');
  const sidebarLinks = document.querySelectorAll('[data-spy-link]');

  if (sections.length && sidebarLinks.length) {
    const spyObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('data-spy-section');
          sidebarLinks.forEach(link => {
            link.classList.toggle('active', link.getAttribute('data-spy-link') === id);
          });
        }
      });
    }, {
      threshold: 0.3,
      rootMargin: '-80px 0px -60% 0px'
    });

    sections.forEach(section => spyObserver.observe(section));
  }

  // ═══════════ EXPANDABLE TECHNIQUE CARDS ═══════════
  document.querySelectorAll('.technique-card').forEach(card => {
    const toggle = () => card.classList.toggle('expanded');
    card.addEventListener('click', toggle);
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggle();
      }
    });
  });
}

// Run on initial page load
document.addEventListener('DOMContentLoaded', initScrollReveals);

// Re-run after Astro View Transition navigations
document.addEventListener('astro:page-load', initScrollReveals);
