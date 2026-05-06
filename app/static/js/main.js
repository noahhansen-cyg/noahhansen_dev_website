// Mobile nav toggle
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');

navToggle.addEventListener('click', () => {
  const expanded = navToggle.getAttribute('aria-expanded') === 'true';
  navToggle.setAttribute('aria-expanded', String(!expanded));
  navLinks.classList.toggle('open');
});

navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
  });
});

// Contact form
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
  const statusEl = contactForm.querySelector('.form-status');
  const submitBtn = contactForm.querySelector('button[type="submit"]');

  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    submitBtn.disabled = true;
    statusEl.textContent = '';
    statusEl.className = 'form-status';

    try {
      const resp = await fetch('/contact', {
        method: 'POST',
        body: new FormData(contactForm),
      });
      const data = await resp.json();
      if (resp.ok && data.success) {
        statusEl.textContent = 'Message sent! I\'ll get back to you soon.';
        statusEl.classList.add('form-status--success');
        contactForm.reset();
      } else {
        statusEl.textContent = data.error || 'Something went wrong. Please try again.';
        statusEl.classList.add('form-status--error');
      }
    } catch {
      statusEl.textContent = 'Network error. Please try again.';
      statusEl.classList.add('form-status--error');
    } finally {
      submitBtn.disabled = false;
    }
  });
}

// Scroll hint fade
const scrollHint = document.querySelector('.scroll-hint');
if (scrollHint) {
  window.addEventListener('scroll', () => {
    const fade = Math.max(0, 1 - window.scrollY / 150);
    scrollHint.style.opacity = fade;
  }, { passive: true });
}

// Theme toggle
const themeToggle = document.querySelector('.theme-toggle');

themeToggle.addEventListener('click', () => {
  document.documentElement.classList.add('theme-transitioning');

  const isLight = document.documentElement.getAttribute('data-theme') === 'light';
  if (isLight) {
    document.documentElement.removeAttribute('data-theme');
    localStorage.setItem('theme', 'dark');
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
  }

  setTimeout(() => document.documentElement.classList.remove('theme-transitioning'), 300);
});
