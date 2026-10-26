import Gumshoe from "./gumshoe-patched.js";

////////////////////////////////////////////////////////////////////////////////
// Scroll Handling
////////////////////////////////////////////////////////////////////////////////
var tocScroll = null;
var header = null;
var lastScrollTop = document.documentElement.scrollTop;
const GO_TO_TOP_OFFSET = 64;

function scrollHandlerForHeader(positionY) {
  if (positionY > 0) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
}

function scrollHandlerForBackToTop(positionY) {
  if (positionY < GO_TO_TOP_OFFSET) {
    document.documentElement.classList.remove("show-back-to-top");
  } else {
    if (positionY < lastScrollTop) {
      document.documentElement.classList.add("show-back-to-top");
    } else if (positionY > lastScrollTop) {
      document.documentElement.classList.remove("show-back-to-top");
    }
  }
  lastScrollTop = positionY;
}

function revealActiveTocLink(link) {
  if (!link || !tocScroll.clientHeight) {
    return;
  }

  const viewport = tocScroll.getBoundingClientRect();
  const row = link.getBoundingClientRect();
  const bottom = Math.min(viewport.bottom, window.innerHeight);
  const hidden = !link.getClientRects().length;
  if (hidden || row.top < viewport.top || row.bottom > bottom) {
    tocScroll.scrollTo({
      top: hidden
        ? 0
        : tocScroll.scrollTop +
          row.top -
          viewport.top -
          (bottom - viewport.top - row.height) / 2,
      behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches
        ? "instant"
        : "smooth",
    });
  }
}

function scrollHandler(positionY) {
  scrollHandlerForHeader(positionY);
  scrollHandlerForBackToTop(positionY);
  if (positionY === 0 && tocScroll !== null) {
    tocScroll.scrollTo({
      top: 0,
      behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches
        ? "instant"
        : "smooth",
    });
  }
}

////////////////////////////////////////////////////////////////////////////////
// Theme Toggle
////////////////////////////////////////////////////////////////////////////////
function setTheme(mode) {
  if (mode !== "light" && mode !== "dark" && mode !== "auto") {
    console.error(`Got invalid theme mode: ${mode}. Resetting to auto.`);
    mode = "auto";
  }

  document.body.dataset.theme = mode;
  localStorage.setItem("theme", mode);
  console.log(`Changed to ${mode} mode.`);
}

function cycleThemeOnce() {
  const currentTheme = localStorage.getItem("theme") || "auto";
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

  if (prefersDark) {
    // Auto (dark) -> Light -> Dark
    if (currentTheme === "auto") {
      setTheme("light");
    } else if (currentTheme == "light") {
      setTheme("dark");
    } else {
      setTheme("auto");
    }
  } else {
    // Auto (light) -> Dark -> Light
    if (currentTheme === "auto") {
      setTheme("dark");
    } else if (currentTheme == "dark") {
      setTheme("light");
    } else {
      setTheme("auto");
    }
  }
}

////////////////////////////////////////////////////////////////////////////////
// Setup
////////////////////////////////////////////////////////////////////////////////
function setupScrollHandler() {
  // Taken from https://developer.mozilla.org/en-US/docs/Web/API/Document/scroll_event
  let last_known_scroll_position = 0;
  let ticking = false;

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

  let activeLink = null;
  tocScroll.addEventListener("gumshoeActivate", (event) => {
    activeLink = event.detail.link;
    revealActiveTocLink(activeLink);
  });
  tocScroll.addEventListener("gumshoeDeactivate", () => {
    activeLink = null;
  });

  // Recheck when resizing or opening the mobile table of contents.
  new ResizeObserver(() => revealActiveTocLink(activeLink)).observe(tocScroll);

  // Scrollspy -- highlight table on contents, based on scroll
  new Gumshoe(".toc-tree a", {
    reflow: true,
    recursive: true,
    navClass: "scroll-current",
    offset: () => {
      let rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
      const headerRect = header.getBoundingClientRect();
      return headerRect.top + headerRect.height + 2.5 * rem + 1;
    },
  });
}

function setupTheme() {
  // Attach event handlers for toggling themes
  const buttons = document.getElementsByClassName("theme-toggle");
  Array.from(buttons).forEach((btn) => {
    btn.addEventListener("click", cycleThemeOnce);
  });
}

function setup() {
  setupTheme();
  setupScrollHandler();
  setupScrollSpy();
}

////////////////////////////////////////////////////////////////////////////////
// Main entrypoint
////////////////////////////////////////////////////////////////////////////////
function main() {
  document.body.parentNode.classList.remove("no-js");

  header = document.querySelector("header");
  tocScroll = document.querySelector(".toc-scroll");

  setup();
}

document.addEventListener("DOMContentLoaded", main);
