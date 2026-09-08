/* ModaVibe — interactions autonomes. Placez ce fichier dans votre dossier static/js/. */
(function () {
  'use strict';

  const menuButton = document.querySelector('[data-menu-toggle]');
  const navigation = document.querySelector('#main-nav');
  const toast = document.querySelector('#toast');
  let toastTimer;

  function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('visible');
    window.clearTimeout(toastTimer);
    toastTimer = window.setTimeout(() => toast.classList.remove('visible'), 2400);
  }

  if (menuButton && navigation) {
    menuButton.addEventListener('click', function () {
      const open = navigation.classList.toggle('is-open');
      menuButton.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
      menuButton.querySelector('span').textContent = open ? '×' : '☰';
    });

    navigation.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navigation.classList.remove('is-open');
        menuButton.querySelector('span').textContent = '☰';
        menuButton.setAttribute('aria-label', 'Ouvrir le menu');
      });
    });
  }

  document.querySelectorAll('[data-scroll]').forEach(function (button) {
    button.addEventListener('click', function () {
      const rail = document.getElementById(button.dataset.scroll);
      if (!rail) return;
      const amount = button.dataset.direction === 'next' ? 330 : -330;
      rail.scrollBy({ left: amount, behavior: 'smooth' });
    });
  });

  const categoryRail = document.querySelector('#category-rail');
  const activeCategory = document.querySelector('#active-category');
  const initialFilter = new URLSearchParams(window.location.search).get('style');
  if (initialFilter && categoryRail) {
    const initialButton = categoryRail.querySelector(`[data-category="${initialFilter}"]`);
    if (initialButton) initialButton.click();
  }
  document.querySelectorAll('[data-category]').forEach(function (button) {
    button.addEventListener('click', function (event) {
      event.preventDefault();
      const selectedCategory = button.dataset.category;
      document.querySelectorAll('[data-category]').forEach((item) => item.classList.remove('selected'));
      button.classList.add('selected');
      document.querySelectorAll('[data-product-style]').forEach(function (product) {
        const visible = selectedCategory === '__all__' || product.dataset.productStyle.toLowerCase() === selectedCategory.toLowerCase();
        product.style.display = visible ? '' : 'none';
      });
      if (activeCategory) activeCategory.textContent = selectedCategory === '__all__' ? 'Tous' : selectedCategory;
      showToast(selectedCategory === '__all__' ? 'Tous les articles affichés' : selectedCategory + ' : sélection activée');
      if (productRail) productRail.scrollTo({ left: 0, behavior: 'smooth' });
    });
  });

  if (categoryRail && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    let categoryAutoScroll;
    const moveCategory = function () {
      const maxScroll = categoryRail.scrollWidth - categoryRail.clientWidth;
      if (maxScroll <= 0) return;
      const next = categoryRail.scrollLeft + 180;
      categoryRail.scrollTo({ left: next >= maxScroll ? 0 : next, behavior: 'smooth' });
    };
    const startCategoryAutoScroll = function () {
      window.clearInterval(categoryAutoScroll);
      categoryAutoScroll = window.setInterval(moveCategory, 4200);
    };
    const stopCategoryAutoScroll = function () {
      window.clearInterval(categoryAutoScroll);
    };
    startCategoryAutoScroll();
    categoryRail.addEventListener('wheel', stopCategoryAutoScroll, { passive: true });
    categoryRail.addEventListener('touchstart', stopCategoryAutoScroll, { passive: true });
    categoryRail.addEventListener('mousedown', stopCategoryAutoScroll);
    categoryRail.addEventListener('pointerdown', stopCategoryAutoScroll);
  }

  const productRail = document.querySelector('#product-rail');
  if (productRail && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    let productAutoScroll;
    const moveProducts = function () {
      const maxScroll = productRail.scrollWidth - productRail.clientWidth;
      const next = productRail.scrollLeft + 343;
      productRail.scrollTo({ left: next >= maxScroll - 4 ? 0 : next, behavior: 'smooth' });
    };
    const startProductAutoScroll = function () {
      window.clearInterval(productAutoScroll);
      productAutoScroll = window.setInterval(moveProducts, 3500);
    };
    const stopProductAutoScroll = function () {
      window.clearInterval(productAutoScroll);
    };
    startProductAutoScroll();
    productRail.addEventListener('mouseenter', stopProductAutoScroll);
    productRail.addEventListener('mouseleave', stopProductAutoScroll);
    productRail.addEventListener('focusin', stopProductAutoScroll);
    productRail.addEventListener('focusout', stopProductAutoScroll);
    productRail.addEventListener('wheel', stopProductAutoScroll, { passive: true });
    productRail.addEventListener('touchstart', stopProductAutoScroll, { passive: true });
    productRail.addEventListener('mousedown', stopProductAutoScroll);
    productRail.addEventListener('pointerdown', stopProductAutoScroll);
  }

  document.querySelectorAll('[data-favorite]').forEach(function (button) {
    button.addEventListener('click', function () {
      const liked = button.classList.toggle('liked');
      button.textContent = liked ? '♥' : '♡';
      button.setAttribute('aria-label', liked ? 'Retirer des favoris' : 'Ajouter aux favoris');
      showToast(liked ? 'Ajouté à vos favoris.' : 'Retiré de vos favoris.');
    });
  });

  document.querySelectorAll('[data-toast]').forEach(function (button) {
    button.addEventListener('click', function () { showToast(button.dataset.toast); });
  });

  document.querySelector('[data-focus-search]')?.addEventListener('click', function () {
    document.querySelector('#search-input')?.focus();
  });

  document.querySelector('#newsletter-form')?.addEventListener('submit', function (event) {
    event.preventDefault();
    showToast('Vous êtes sur la liste. À très vite !');
    event.currentTarget.reset();
  });

  document.querySelector('#search-input')?.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
      event.preventDefault();
      showToast('Recherche prête à être connectée à votre catalogue.');
    }
  });
})();




document.addEventListener("DOMContentLoaded", function () {

    const whatsappNumber = "{{ whatsapp_number|default:'' }}";

    document.querySelectorAll(".whatsapp-order").forEach(function (button) {

        button.addEventListener("click", function (event) {
            event.preventDefault();

            const name = this.dataset.productName;
            const price = this.dataset.productPrice;
            const oldPrice = this.dataset.productOldPrice;
            const discount = this.dataset.productDiscount;
            const image = this.dataset.productImage;

            const message =
`Bonjour 👋

Je souhaite commander cet article :

🛍️ Produit : ${name}
💰 Prix : ${price}
🏷️ Ancien prix : ${oldPrice}
🔥 Remise : ${discount}

🖼️ Image du produit :
${image}

Merci de me confirmer la disponibilité.`;

            const whatsappUrl =
                "https://wa.me/" +
                whatsappNumber +
                "?text=" +
                encodeURIComponent(message);

            window.open(whatsappUrl, "_blank");
        });

    });

});
