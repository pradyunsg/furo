////////////////////////////////////////////////////////////////////////////////
// Scroll Handling
////////////////////////////////////////////////////////////////////////////////
var tocScroll = null;
var header = null;

function scrollHandlerForHeader() {
  if (Math.floor(header.getBoundingClientRect().top) == 0) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
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

// Custom flyte theme logic
var toggleCurrentSubsection = function() {
  // only show currently selected subsection
  $(".sidebar-tree").children("ul.current").each(function() {
    $(this).css("display", "block");
    $(this).prev("p.caption").css("display", "block");
  });
}

var highlightCurrentSubsection = function() {
  // highlight the current subsection in the main nav
  var currentSection = $(".sidebar-tree").children("ul.current");
  var caption = currentSection.prev("p.caption").text();
  var mainNav = $(".sidebar-tree").children("ul").first();
  mainNav.find("li a").each(function() {
      if ($(this).text() === caption) {
          $(this).css("font-weight", "bold");
      }
  })
}

function main() {
  document.body.parentNode.classList.remove("no-js");

  header = document.querySelector("header");
  tocScroll = document.querySelector(".toc-scroll");

  setup();

  toggleCurrentSubsection();
  highlightCurrentSubsection();

  // custom scrolling on toc
  setTimeout(function() {
    sidebar = document.querySelector(".sidebar-scroll");
    target = document.querySelector(".current-page");
    sidebar.scrollTo(0, target.offsetTop + 200);

    jQuery(".sidebar-scroll").animate({opacity: 1.0}, 100);
  }, 10);
}

document.addEventListener("DOMContentLoaded", main);
