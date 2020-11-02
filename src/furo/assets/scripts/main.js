////////////////////////////////////////////////////////////////////////////////
// Scroll Handling
////////////////////////////////////////////////////////////////////////////////
var tocScroll = null;
var header = null;

function scrollHandlerForHeader() {
  if (header.getBoundingClientRect().top == 0) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
}

function scrollHandlerForTOC(positionY) {
  if (tocScroll === null) {
    return;
  }

  if (positionY == 0) {
    tocScroll.scrollTo(0, 0);
  }
}

function scrollHandler(positionY) {
  scrollHandlerForHeader();
  scrollHandlerForTOC(positionY);
}

////////////////////////////////////////////////////////////////////////////////
// Setup
////////////////////////////////////////////////////////////////////////////////
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

function setupScrollSpy() {
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

function setup() {
  setupScrollHandler();
  setupScrollSpy();
}

function main() {
  document.body.parentNode.classList.remove("no-js");

  header = document.querySelector("header");
  tocScroll = document.querySelector(".toc-scroll");

  setup();
}

document.addEventListener("DOMContentLoaded", main);
