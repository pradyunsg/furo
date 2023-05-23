import Gumshoe from "./gumshoe-patched.js";

////////////////////////////////////////////////////////////////////////////////
// Scroll Handling
////////////////////////////////////////////////////////////////////////////////
var tocScroll = null;
var header = null;
var lastScrollTop = window.pageYOffset || document.documentElement.scrollTop;
const GO_TO_TOP_OFFSET = 64;

function scrollHandlerForHeader() {
  if (Math.floor(header.getBoundingClientRect().top) == 0) {
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

function scrollHandlerForTOC(positionY) {
  if (tocScroll === null) {
    return;
  }

  // top of page.
  if (positionY == 0) {
    tocScroll.scrollTo(0, 0);
  } else if (
    // bottom of page.
    Math.ceil(positionY) >=
    Math.floor(document.documentElement.scrollHeight - window.innerHeight)
  ) {
    tocScroll.scrollTo(0, tocScroll.scrollHeight);
  } else {
    // somewhere in the middle.
    const current = document.querySelector(".scroll-current");
    if (current == null) {
      return;
    }

    // https://github.com/pypa/pip/issues/9159 This breaks scroll behaviours.
    // // scroll the currently "active" heading in toc, into view.
    // const rect = current.getBoundingClientRect();
    // if (0 > rect.top) {
    //   current.scrollIntoView(true); // the argument is "alignTop"
    // } else if (rect.bottom > window.innerHeight) {
    //   current.scrollIntoView(false);
    // }
  }
}

function scrollHandler(positionY) {
  scrollHandlerForHeader();
  scrollHandlerForBackToTop(positionY);
  scrollHandlerForTOC(positionY);
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

  // Scrollspy -- highlight table on contents, based on scroll
  new Gumshoe(".toc-tree a", {
    reflow: true,
    recursive: true,
    navClass: "scroll-current",
    offset: () => {
      let rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
      return header.getBoundingClientRect().height + 0.5 * rem + 1;
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

////////////////////////////////////////////////////////////////////////////////
// Keyboard Accessibility
////////////////////////////////////////////////////////////////////////////////

// Determines which of the two table-of-contents menu labels is visible.
function determineVisibleTocOpenMenu() {
  const mediaQuery = window.matchMedia("(max-width: 67em)");
  return mediaQuery.matches ? "toc-menu-open-sm" : "toc-menu-open-md";
}

// A mapping of current to next focus id's. For example, We want a corresponsing
// menu's close button to be highlighted after a menu is opened with a keyboard.
const NEXT_FOCUS_ID_MAP = {
  "nav-menu-open": "nav-menu-close",
  "nav-menu-close": "nav-menu-open",
  "toc-menu-open-sm": "toc-menu-close",
  "toc-menu-open-md": "toc-menu-close",
  "toc-menu-close": determineVisibleTocOpenMenu(),
};

// Toggles the visibility of a sidebar menu to prevent keyboard focus on hidden elements.
function toggleSidebarMenuVisibility(elementQuery, inputQuery) {
  const sidebarElement = document.querySelector(elementQuery);
  const sidebarInput = document.querySelector(inputQuery);
  sidebarInput.addEventListener("change", () => {
    setTimeout(
      () => {
        sidebarElement.classList.toggle("hide-sidebar", !sidebarInput.checked);
      },
      sidebarInput.checked ? 0 : 250,
    );
  });
  window.matchMedia("(max-width: 67em)").addEventListener("change", (event) => {
    NEXT_FOCUS_ID_MAP["toc-menu-close"] = determineVisibleTocOpenMenu();
    if (!event.matches) {
      document
        .querySelector(".sidebar-drawer")
        .classList.remove("hide-sidebar");
    }
  });
  window.matchMedia("(max-width: 82em)").addEventListener("change", (event) => {
    if (!event.matches) {
      document.querySelector(".toc-drawer").classList.remove("hide-sidebar");
    }
  });
}

// Activates labels when a user focuses on them and clicks "Enter".
// Also highlights the next appropriate input label.
function activateLabelOnEnter() {
  const labels = document.querySelectorAll("label");
  labels.forEach((element) => {
    element.addEventListener("keypress", (event) => {
      if (event.key === "Enter") {
        const targetId = element.getAttribute("for");
        document.getElementById(targetId).click();
        const nextFocusId = NEXT_FOCUS_ID_MAP[element.id];
        if (nextFocusId) {
          // Timeout is needed to let the label become visible.
          setTimeout(() => {
            document.getElementById(nextFocusId).focus();
          }, 250);
        }
      }
    });
  });
}

// Improves accessibility for keyboard-only users.
function setupKeyboardFriendlyNavigation() {
  activateLabelOnEnter();
  toggleSidebarMenuVisibility(".toc-drawer", "#__toc");
  toggleSidebarMenuVisibility(".sidebar-drawer", "#__navigation");
}

function setup() {
  setupTheme();
  setupScrollHandler();
  setupScrollSpy();
  setupKeyboardFriendlyNavigation();
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
