document.addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector(".site-header");
  const navLinks = document.querySelectorAll(".navbar-nav .nav-link");
  const yearEl = document.getElementById("year");
  const form = document.querySelector("form.needs-validation");

  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  const onScroll = () => {
    if (!header) return;
    header.style.boxShadow = window.scrollY > 8 ? "0 8px 24px rgba(11,31,58,.06)" : "none";
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  navLinks.forEach((link) => {
    const href = link.getAttribute("href");
    if (href && href === window.location.pathname) {
      link.classList.add("active");
    }
  });

  if (form) {
    form.addEventListener("submit", (event) => {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add("was-validated");
    });
  }

  document.querySelectorAll("[data-count]").forEach((el) => {
    const target = Number(el.dataset.count);
    const suffix = el.dataset.suffix || "";
    let current = 0;
    const step = Math.max(1, Math.round(target / 40));
    const tick = () => {
      current = Math.min(target, current + step);
      el.textContent = `${current}${suffix}`;
      if (current < target) requestAnimationFrame(tick);
    };
    tick();
  });
});
