/* ===== PRODUCT PAGE JS ===== */
(function() {
  'use strict';

  // ===== GALLERY =====
  const gallery = {
    currentIndex: 0,
    images: [],

    init() {
      const mainImg = document.querySelector('.gallery-main img');
      const thumbs = document.querySelectorAll('.gallery-thumb');
      const prevBtn = document.querySelector('.gallery-prev');
      const nextBtn = document.querySelector('.gallery-next');
      const zoomBtn = document.querySelector('.gallery-zoom');
      const mainWrap = document.querySelector('.gallery-main');

      if (!mainImg || !thumbs.length) return;

      this.images = Array.from(thumbs).map(t => ({
        src: t.dataset.full || t.querySelector('img').src,
        alt: t.querySelector('img').alt || ''
      }));

      thumbs.forEach((thumb, i) => {
        thumb.addEventListener('click', () => this.goTo(i));
      });

      if (prevBtn) prevBtn.addEventListener('click', () => this.prev());
      if (nextBtn) nextBtn.addEventListener('click', () => this.next());
      if (zoomBtn) zoomBtn.addEventListener('click', () => this.openLightbox());
      if (mainWrap) mainWrap.addEventListener('click', (e) => {
        if (e.target.tagName !== 'BUTTON') this.openLightbox();
      });

      // Keyboard navigation
      document.addEventListener('keydown', (e) => {
        if (document.querySelector('.lightbox.active')) {
          if (e.key === 'Escape') this.closeLightbox();
          if (e.key === 'ArrowLeft') this.lightboxPrev();
          if (e.key === 'ArrowRight') this.lightboxNext();
        }
      });

      this.update();
    },

    goTo(index) {
      this.currentIndex = index;
      this.update();
    },

    prev() {
      this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
      this.update();
    },

    next() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
      this.update();
    },

    update() {
      const mainImg = document.querySelector('.gallery-main img');
      const thumbs = document.querySelectorAll('.gallery-thumb');
      const prevBtn = document.querySelector('.gallery-prev');
      const nextBtn = document.querySelector('.gallery-next');

      if (mainImg && this.images[this.currentIndex]) {
        mainImg.src = this.images[this.currentIndex].src;
        mainImg.alt = this.images[this.currentIndex].alt;
      }

      thumbs.forEach((t, i) => {
        t.classList.toggle('active', i === this.currentIndex);
      });

      if (prevBtn) prevBtn.style.display = this.images.length <= 1 ? 'none' : '';
      if (nextBtn) nextBtn.style.display = this.images.length <= 1 ? 'none' : '';

      // Scroll thumb into view
      if (thumbs[this.currentIndex]) {
        thumbs[this.currentIndex].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
      }
    },

    openLightbox() {
      if (!this.images.length) return;
      let lb = document.querySelector('.lightbox');
      if (!lb) {
        lb = document.createElement('div');
        lb.className = 'lightbox';
        lb.innerHTML = `
          <button class="lightbox-close">&times;</button>
          <button class="lightbox-nav lightbox-prev">&#8249;</button>
          <button class="lightbox-nav lightbox-next">&#8250;</button>
          <img src="" alt="">
          <div class="lightbox-counter"></div>
        `;
        document.body.appendChild(lb);

        lb.querySelector('.lightbox-close').addEventListener('click', () => this.closeLightbox());
        lb.querySelector('.lightbox-prev').addEventListener('click', (e) => { e.stopPropagation(); this.lightboxPrev(); });
        lb.querySelector('.lightbox-next').addEventListener('click', (e) => { e.stopPropagation(); this.lightboxNext(); });
        lb.addEventListener('click', (e) => {
          if (e.target === lb) this.closeLightbox();
        });
      }
      this.updateLightbox();
      lb.classList.add('active');
      document.body.style.overflow = 'hidden';
    },

    closeLightbox() {
      const lb = document.querySelector('.lightbox');
      if (lb) {
        lb.classList.remove('active');
        document.body.style.overflow = '';
      }
    },

    lightboxPrev() {
      this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
      this.update();
      this.updateLightbox();
    },

    lightboxNext() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
      this.update();
      this.updateLightbox();
    },

    updateLightbox() {
      const lb = document.querySelector('.lightbox');
      if (!lb) return;
      const img = lb.querySelector('img');
      const counter = lb.querySelector('.lightbox-counter');
      if (img && this.images[this.currentIndex]) {
        img.src = this.images[this.currentIndex].src;
        img.alt = this.images[this.currentIndex].alt;
      }
      if (counter) {
        counter.textContent = `${this.currentIndex + 1} / ${this.images.length}`;
      }
    }
  };

  // ===== VARIANT SELECTOR =====
  const variantPicker = {
    selectedVariant: null,
    variants: [],

    init() {
      const container = document.querySelector('.variant-options');
      if (!container) return;

      // Read variant data from data attribute
      const variantData = document.querySelector('[data-variants]');
      if (variantData) {
        try {
          this.variants = JSON.parse(variantData.dataset.variants);
        } catch(e) {}
      }

      const buttons = container.querySelectorAll('.variant-btn');
      buttons.forEach(btn => {
        btn.addEventListener('click', () => {
          if (btn.classList.contains('out-of-stock')) return;
          buttons.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          this.selectedVariant = btn.dataset.variantId;
          this.onVariantChange(btn.dataset);
        });
      });

      // Set first in-stock variant as default
      const firstActive = container.querySelector('.variant-btn.active') || container.querySelector('.variant-btn:not(.out-of-stock)');
      if (firstActive) {
        this.selectedVariant = firstActive.dataset.variantId;
      }
    },

    onVariantChange(data) {
      // Update price display
      const priceEl = document.querySelector('.price-current');
      if (priceEl && data.price) {
        priceEl.textContent = '₹' + data.price;
      }

      // Update original price
      const origEl = document.querySelector('.price-original');
      if (origEl && data.comparePrice) {
        origEl.textContent = '₹' + data.comparePrice;
        origEl.style.display = '';
      } else if (origEl) {
        origEl.style.display = 'none';
      }

      // Update discount badge
      const discEl = document.querySelector('.price-discount');
      if (discEl && data.comparePrice && data.price) {
        const discount = Math.round((1 - parseInt(data.price.replace(/,/g,'')) / parseInt(data.comparePrice.replace(/,/g,''))) * 100);
        if (discount > 0) {
          discEl.textContent = discount + '% OFF';
          discEl.style.display = '';
        } else {
          discEl.style.display = 'none';
        }
      }

      // Update hidden form input
      const idInput = document.querySelector('#variant-id');
      if (idInput && data.variantId) {
        idInput.value = data.variantId;
      }

      // Update unit price
      const unitEl = document.querySelector('.variant-unit-price');
      if (unitEl && data.unitPrice) {
        unitEl.textContent = data.unitPrice;
      }
    }
  };

  // ===== QUANTITY SELECTOR =====
  const quantitySelector = {
    init() {
      const container = document.querySelector('.quantity-selector');
      if (!container) return;

      const input = container.querySelector('.qty-input');
      const decreaseBtn = container.querySelector('.qty-decrease');
      const increaseBtn = container.querySelector('.qty-increase');

      if (decreaseBtn) {
        decreaseBtn.addEventListener('click', () => {
          const val = parseInt(input.value) || 1;
          if (val > 1) {
            input.value = val - 1;
            this.updateButtons(input);
          }
        });
      }

      if (increaseBtn) {
        increaseBtn.addEventListener('click', () => {
          const val = parseInt(input.value) || 1;
          if (val < 10) {
            input.value = val + 1;
            this.updateButtons(input);
          }
        });
      }

      this.updateButtons(input);
    },

    updateButtons(input) {
      const container = input.closest('.quantity-selector');
      const decreaseBtn = container.querySelector('.qty-decrease');
      const increaseBtn = container.querySelector('.qty-increase');
      const val = parseInt(input.value) || 1;
      if (decreaseBtn) decreaseBtn.disabled = val <= 1;
      if (increaseBtn) increaseBtn.disabled = val >= 10;
    }
  };

  // ===== ADD TO CART =====
  const cart = {
    items: [],

    init() {
      const cartBtn = document.querySelector('.btn-cart');
      const buyBtn = document.querySelector('.btn-buy');

      if (cartBtn) {
        cartBtn.addEventListener('click', (e) => {
          e.preventDefault();
          this.addToCart();
        });
      }

      if (buyBtn) {
        buyBtn.addEventListener('click', (e) => {
          e.preventDefault();
          this.buyNow();
        });
      }

      // Load from localStorage
      try {
        const saved = localStorage.getItem('tbof_cart');
        if (saved) this.items = JSON.parse(saved);
      } catch(e) {}
    },

    addToCart() {
      const qtyInput = document.querySelector('.qty-input');
      const qty = parseInt(qtyInput?.value) || 1;
      const activeVariant = document.querySelector('.variant-btn.active');
      const productName = document.querySelector('.product-title')?.textContent?.trim();
      const productImg = document.querySelector('.gallery-thumb.active img')?.src;
      const price = activeVariant?.dataset.price || document.querySelector('.price-current')?.textContent?.replace('₹','').replace(/,/g,'');
      const variantId = activeVariant?.dataset.variantId || 'default';
      const variantName = activeVariant?.querySelector('.variant-name')?.textContent?.trim() || '';

      const item = {
        id: variantId,
        name: productName,
        variant: variantName,
        price: parseInt(price?.replace(/,/g,'')) || 0,
        qty: qty,
        image: productImg
      };

      // Check if variant already in cart
      const existing = this.items.find(i => i.id === variantId);
      if (existing) {
        existing.qty += qty;
      } else {
        this.items.push(item);
      }

      // Save to localStorage
      try {
        localStorage.setItem('tbof_cart', JSON.stringify(this.items));
      } catch(e) {}

      // Show notification
      this.showNotification(`${productName} added to cart!`);

      // Update cart count
      this.updateCartCount();

      // Animate button
      const cartBtn = document.querySelector('.btn-cart');
      if (cartBtn) {
        cartBtn.textContent = '✓ ADDED';
        cartBtn.style.background = '#27ae60';
        setTimeout(() => {
          cartBtn.textContent = 'ADD TO CART';
          cartBtn.style.background = '';
        }, 1500);
      }
    },

    buyNow() {
      this.addToCart();
      // Redirect to checkout (or show message in static context)
      setTimeout(() => {
        alert('Checkout functionality requires a live Shopify store. Your items are saved in the cart.');
      }, 500);
    },

    showNotification(message) {
      let notif = document.querySelector('.cart-notification');
      if (!notif) {
        notif = document.createElement('div');
        notif.className = 'cart-notification';
        notif.innerHTML = '<span class="check">✓</span><span class="msg"></span>';
        document.body.appendChild(notif);
      }
      notif.querySelector('.msg').textContent = message;
      notif.classList.add('show');
      setTimeout(() => notif.classList.remove('show'), 3000);
    },

    updateCartCount() {
      const count = this.items.reduce((sum, item) => sum + item.qty, 0);
      const badge = document.querySelector('.cart-count');
      if (badge) {
        badge.textContent = count;
        badge.style.display = count > 0 ? '' : 'none';
      }
    }
  };

  // ===== PINCODE CHECKER =====
  const pincodeChecker = {
    init() {
      const btn = document.querySelector('.pincode-btn');
      const input = document.querySelector('.pincode-input');
      const result = document.querySelector('.pincode-result');
      const loading = document.querySelector('.pincode-loading');

      if (!btn || !input) return;

      btn.addEventListener('click', () => {
        const code = input.value.trim();
        if (!code || code.length !== 6 || !/^\d+$/.test(code)) {
          result.className = 'pincode-result error';
          result.textContent = 'Please enter a valid 6-digit PIN code';
          return;
        }

        loading.classList.add('active');
        result.className = 'pincode-result';
        result.textContent = '';

        // Simulate delivery check (in real implementation, this would call an API)
        setTimeout(() => {
          loading.classList.remove('active');
          // Common Indian PIN code ranges for metro cities
          const metroPrefixes = ['110', '400', '560', '600', '700', '500', '380', '411', '302', '226', '403', '682', '560', '695'];
          const prefix = code.substring(0, 3);
          const isMetro = metroPrefixes.includes(prefix);

          if (isMetro) {
            result.className = 'pincode-result success';
            result.innerHTML = '<strong>✓ Delivery Available</strong><br>Estimated delivery: 3-5 business days';
          } else {
            result.className = 'pincode-result success';
            result.innerHTML = '<strong>✓ Delivery Available</strong><br>Estimated delivery: 5-7 business days';
          }
        }, 1200);
      });

      input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') btn.click();
      });
    }
  };

  // ===== FAQ ACCORDION =====
  const faqAccordion = {
    init() {
      const items = document.querySelectorAll('.faq-item');
      items.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (question) {
          question.addEventListener('click', () => {
            const wasOpen = item.classList.contains('open');
            // Close all others
            items.forEach(i => i.classList.remove('open'));
            if (!wasOpen) item.classList.add('open');
          });
        }
      });
    }
  };

  // ===== STICKY ADD TO CART (MOBILE) =====
  const stickyATC = {
    init() {
      const stickyEl = document.querySelector('.sticky-atc');
      const mainBtn = document.querySelector('.btn-cart');
      if (!stickyEl || !mainBtn) return;

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (window.innerWidth <= 999) {
            stickyEl.classList.toggle('visible', !entry.isIntersecting);
          }
        });
      }, { threshold: 0 });

      observer.observe(mainBtn);

      // Sync sticky button with main
      const stickyBtn = stickyEl.querySelector('.btn-cart');
      if (stickyBtn) {
        stickyBtn.addEventListener('click', (e) => {
          e.preventDefault();
          mainBtn.click();
        });
      }

      window.addEventListener('resize', () => {
        if (window.innerWidth > 999) {
          stickyEl.classList.remove('visible');
        }
      });
    }
  };

  // ===== TABS (Description, Ingredients, etc.) =====
  const detailTabs = {
    init() {
      const tabs = document.querySelectorAll('.detail-tab');
      tabs.forEach(tab => {
        tab.querySelector('summary')?.addEventListener('click', (e) => {
          // Native details element handles open/close
        });
      });
    }
  };

  // ===== INITIALIZE =====
  document.addEventListener('DOMContentLoaded', () => {
    gallery.init();
    variantPicker.init();
    quantitySelector.init();
    cart.init();
    pincodeChecker.init();
    faqAccordion.init();
    stickyATC.init();
    detailTabs.init();

    // Set first variant as active
    const firstBtn = document.querySelector('.variant-btn:not(.out-of-stock)');
    if (firstBtn && !document.querySelector('.variant-btn.active')) {
      firstBtn.classList.add('active');
    }
  });

})();
