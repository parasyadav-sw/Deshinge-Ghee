/* Shared JavaScript for consistent functionality across all pages */

/* ===== Typing Placeholder Animation ===== */
function initTypingPlaceholder() {
  var searchInputBoxSelector = document.querySelectorAll('.st-searchbox input');

  searchInputBoxSelector.forEach(function(searchInputBox) {
    if (searchInputBox && !searchInputBox.dataset.typingInit) {
      searchInputBox.dataset.typingInit = 'true';
      searchInputBox.setAttribute('placeholder', '');
      searchInputBox.parentElement.classList.add('typing-placeholder');

      var typingEl = document.createElement('span');
      typingEl.classList.add('typing-text');

      var cursorEl = document.createElement('span');
      cursorEl.classList.add('typing-cursor');

      typingEl.appendChild(cursorEl);
      searchInputBox.parentElement.appendChild(typingEl);

      var phrases = ['Search For Ghee'];
      var phraseIndex = 0;
      var charIndex = 0;
      var isDeleting = false;
      var isStopped = false;
      var typingInterval = null;

      function type() {
        if (isStopped) return;

        var currentPhrase = phrases[phraseIndex];

        if (!isDeleting) {
          cursorEl.style.display = 'inline-block';
          typingEl.textContent = currentPhrase.substring(0, charIndex + 1);
          typingEl.appendChild(cursorEl);
          charIndex++;

          if (charIndex === currentPhrase.length) {
            setTimeout(function() {
              isDeleting = true;
              type();
            }, 2000);
            return;
          }
          typingInterval = setTimeout(type, 100);
        } else {
          typingEl.textContent = currentPhrase.substring(0, charIndex - 1);
          typingEl.appendChild(cursorEl);
          charIndex--;

          if (charIndex === 0) {
            isDeleting = false;
            phraseIndex = (phraseIndex + 1) % phrases.length;
            typingInterval = setTimeout(type, 500);
            return;
          }
          typingInterval = setTimeout(type, 50);
        }
      }

      type();

      searchInputBox.addEventListener('focus', function() {
        isStopped = true;
        if (typingInterval) clearTimeout(typingInterval);
        typingEl.style.display = 'none';
      });

      searchInputBox.addEventListener('blur', function() {
        if (!searchInputBox.value) {
          isStopped = false;
          typingEl.style.display = 'block';
          charIndex = 0;
          isDeleting = false;
          phraseIndex = (phraseIndex + 1) % phrases.length;
          type();
        }
      });

      searchInputBox.addEventListener('input', function() {
        if (searchInputBox.value) {
          typingEl.style.display = 'none';
        } else {
          typingEl.style.display = 'block';
        }
      });
    }
  });
}

/* ===== Fix Search Form Actions ===== */
function fixSearchFormActions() {
  var searchForms = document.querySelectorAll('.main-search__form[action="#"], .main-search__form[action=""]');
  searchForms.forEach(function(form) {
    form.setAttribute('action', '/search');
    form.setAttribute('method', 'get');
  });
}

/* ===== Fix Footer Newsletter Form Actions ===== */
function fixFooterFormActions() {
  var footerForms = document.querySelectorAll('.footer__newsletter-form[action="#"], .footer__newsletter-form[action=""]');
  footerForms.forEach(function(form) {
    form.setAttribute('action', '/contact#footer-newsletter');
    form.setAttribute('method', 'post');
  });
}

/* ===== Initialize All Shared Functionality ===== */
function initSharedFeatures() {
  initTypingPlaceholder();
  fixSearchFormActions();
  fixFooterFormActions();
}

/* Run on DOM ready */
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initSharedFeatures);
} else {
  initSharedFeatures();
}
