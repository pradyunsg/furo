var header = undefined;
var tocScroll = undefined;

function scrollHandler(positionY) {
  if (positionY == 0) {
    header.classList.remove("scrolled");
  } else {
    header.classList.add("scrolled");
  }

  if (tocScroll === undefined) { return; }

  if (positionY == 0) {
    tocScroll.scrollTo(0, 0);
  } else if (Math.ceil(window.innerHeight + positionY) >= document.body.offsetHeight) {
    tocScroll.scrollTo(0, tocScroll.scrollHeight);
  }
}

function setupScrollHandler() {
  // Taken from https://developer.mozilla.org/en-US/docs/Web/API/Document/scroll_event
  let last_known_scroll_position = 0;
  let ticking = false;

  window.addEventListener('scroll', function(e) {
    last_known_scroll_position = window.scrollY;

    if (!ticking) {
      window.requestAnimationFrame(function() {
        scrollHandler(last_known_scroll_position);
        ticking = false;
      });

      ticking = true;
    }
  });
}

function setup() {
  setupScrollHandler();

  // Scrollspy -- highlight table on contents, based on scroll
  let spy = new Gumshoe(".toc-tree a", {
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
