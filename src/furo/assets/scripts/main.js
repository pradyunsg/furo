(function (window, document) {
  var header = null;
  var tocScroll = null;

  function scrollHandler(positionY) {
    if (header.getBoundingClientRect().top == 0) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }

    if (tocScroll === null) {
      return;
    }

    if (positionY == 0) {
      tocScroll.scrollTo(0, 0);
    }
  }

  function setupScrollHandler() {
    // Taken from https://developer.mozilla.org/en-US/docs/Web/API/Document/scroll_event
    var last_known_scroll_position = 0;
    var ticking = false;

    window.addEventListener("scroll", function (e) {
      last_known_scroll_position = window.scrollY;

      if (!ticking) {
        window.requestAnimationFrame(function () {
          scrollHandler(last_known_scroll_position);
          ticking = false;
        });

        ticking = true;
      }
    });
    window.scroll();
  }

  function setup() {
    setupScrollHandler();

    if (tocScroll === null) {
      return;
    }

    // Scrollspy -- highlight table on contents, based on scroll
    var spy = new Gumshoe(".toc-tree a", {
      reflow: true,
      recursive: true,
      navClass: "scroll-current",
    });
  }

  document.addEventListener("DOMContentLoaded", function main(params) {
    document.body.parentNode.classList.remove("no-js");

    header = document.querySelector("header");
    tocScroll = document.querySelector(".toc-scroll");
    setup();
  });
})(window, document);
