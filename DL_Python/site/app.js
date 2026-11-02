(function(){
  "use strict";

  var LECTURES = window.LECTURES || [];
  var byLecture = {};
  var byTopicKey = {}; // "L-id" -> {lecture, topic}
  var flatTopics = []; // for search + pager, in display order

  LECTURES.forEach(function(lec){
    byLecture[lec.num] = lec;
    lec.topics.forEach(function(t){
      byTopicKey[lec.num + "-" + t.id] = { lecture: lec, topic: t };
      flatTopics.push({ lecture: lec, topic: t });
    });
  });

  var totalTopics = flatTopics.length;

  function lecLabel(lec){
    return lec.label || ("Lecture " + lec.num);
  }

  // ---------------- Lab Assignments data ----------------
  var DIAGRAMS = window.DIAGRAMS || {};

  var LAB_ASSIGNMENTS = window.LAB_ASSIGNMENTS || [];
  var byLab = {};
  var byLabSectionKey = {}; // "N-sectionId" -> {assignment, section}
  var flatLabSections = []; // for search + pager, in display order

  LAB_ASSIGNMENTS.forEach(function(lab){
    byLab[lab.num] = lab;
    lab.sections.forEach(function(s){
      byLabSectionKey[lab.num + "-" + s.id] = { assignment: lab, section: s };
      flatLabSections.push({ assignment: lab, section: s });
    });
  });

  var totalLabQuestions = flatLabSections.filter(function(x){ return x.section.kind === "question"; }).length;

  // ---------------- Theme ----------------
  var root = document.documentElement;
  function applyTheme(mode){
    if(mode === "system"){ root.removeAttribute("data-theme"); }
    else { root.setAttribute("data-theme", mode); }
  }
  var savedTheme = localStorage.getItem("dl-theme") || "system";
  applyTheme(savedTheme);
  document.getElementById("themeToggle").addEventListener("click", function(){
    var current = localStorage.getItem("dl-theme") || "system";
    var isDark = current === "dark" || (current === "system" && window.matchMedia("(prefers-color-scheme: dark)").matches);
    var next = isDark ? "light" : "dark";
    localStorage.setItem("dl-theme", next);
    applyTheme(next);
  });

  // ---------------- Sidebar ----------------
  var sidebarNav = document.getElementById("sidebarNav");
  var sidebar = document.getElementById("sidebar");
  var backdrop = document.getElementById("sidebarBackdrop");
  var menuToggle = document.getElementById("menuToggle");

  function closeSidebarMobile(){
    sidebar.classList.remove("open");
    backdrop.classList.remove("open");
  }
  menuToggle.addEventListener("click", function(){
    sidebar.classList.toggle("open");
    backdrop.classList.toggle("open");
  });
  backdrop.addEventListener("click", closeSidebarMobile);

  function renderSidebar(activeLecNum, activeTopicId, activeLabNum, activeSectionId, activeChat){
    sidebarNav.innerHTML = "";

    // "Ask DL AI" chat nav link disabled for now — DL_Python doesn't need the
    // chatbot yet. Not deleted, just commented out, so it's a one-line
    // uncomment (plus the matching block in the router below) to bring back
    // later if/when the chatbot is wired up for this site.
    // var chatLink = document.createElement("a");
    // chatLink.className = "chat-nav-link" + (activeChat ? " active" : "");
    // chatLink.href = "#/chat";
    // chatLink.innerHTML = '<span class="chat-nav-icon">🤖</span> Ask DL AI';
    // chatLink.addEventListener("click", closeSidebarMobile);
    // sidebarNav.appendChild(chatLink);

    var lecturesLabel = document.createElement("div");
    lecturesLabel.className = "sidebar-section-label";
    lecturesLabel.textContent = "Lectures";
    sidebarNav.appendChild(lecturesLabel);

    LECTURES.forEach(function(lec){
      var group = document.createElement("div");
      group.className = "lecture-group" + (lec.num === activeLecNum ? " open" : "");

      var header = document.createElement("button");
      header.className = "lecture-header";
      header.innerHTML =
        '<span class="lecture-num">' + lec.num + '</span>' +
        '<span class="lecture-title">' + escapeHtml(lec.title) + '</span>' +
        '<svg class="lecture-chevron" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>';
      header.addEventListener("click", function(){
        var willOpen = !group.classList.contains("open");
        group.classList.toggle("open");
        if(willOpen){ location.hash = "#/lecture/" + lec.num; }
      });
      group.appendChild(header);

      var list = document.createElement("div");
      list.className = "topic-list";
      lec.topics.forEach(function(t){
        var a = document.createElement("a");
        a.className = "topic-item" + (lec.num === activeLecNum && t.id === activeTopicId ? " active" : "");
        a.href = "#/lecture/" + lec.num + "/" + t.id;
        a.textContent = t.title;
        a.addEventListener("click", closeSidebarMobile);
        list.appendChild(a);
      });
      group.appendChild(list);
      sidebarNav.appendChild(group);
    });

    if(LAB_ASSIGNMENTS.length){
      var labsLabel = document.createElement("div");
      labsLabel.className = "sidebar-section-label";
      labsLabel.textContent = "Lab Assignments";
      sidebarNav.appendChild(labsLabel);

      LAB_ASSIGNMENTS.forEach(function(lab){
        var group = document.createElement("div");
        group.className = "lecture-group lab-group" + (lab.num === activeLabNum ? " open" : "");

        var header = document.createElement("button");
        header.className = "lecture-header";
        header.innerHTML =
          '<span class="lecture-num lab-num">' + lab.num + '</span>' +
          '<span class="lecture-title">Lab Assignment ' + lab.num + '</span>' +
          '<svg class="lecture-chevron" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>';
        header.addEventListener("click", function(){
          var willOpen = !group.classList.contains("open");
          group.classList.toggle("open");
          if(willOpen){ location.hash = "#/lab/" + lab.num; }
        });
        group.appendChild(header);

        var list = document.createElement("div");
        list.className = "topic-list";
        lab.sections.forEach(function(s){
          var a = document.createElement("a");
          a.className = "topic-item" + (lab.num === activeLabNum && s.id === activeSectionId ? " active" : "");
          a.href = "#/lab/" + lab.num + "/" + s.id;
          a.textContent = sectionSidebarLabel(s);
          a.addEventListener("click", closeSidebarMobile);
          list.appendChild(a);
        });
        group.appendChild(list);
        sidebarNav.appendChild(group);
      });
    }

    document.getElementById("statsLine").textContent =
      LECTURES.length + " lectures · " + totalTopics + " topics · " +
      LAB_ASSIGNMENTS.length + " lab assignments · " + totalLabQuestions + " questions";
  }

  function sectionSidebarLabel(s){
    if(s.kind === "setup") return "Setup";
    if(s.kind === "wrapup") return "Saving Results";
    return "Question " + s.number;
  }

  // ---------------- Search ----------------
  var searchInput = document.getElementById("searchInput");
  var searchResults = document.getElementById("searchResults");
  var searchActiveIndex = -1;
  var currentResults = [];

  function runSearch(q){
    q = q.trim().toLowerCase();
    if(!q){ searchResults.classList.add("hidden"); searchResults.innerHTML = ""; return; }
    var topicResults = flatTopics.filter(function(item){
      return item.topic.title.toLowerCase().indexOf(q) !== -1 ||
             ("lecture " + item.lecture.num).indexOf(q) !== -1 ||
             item.lecture.title.toLowerCase().indexOf(q) !== -1;
    }).map(function(item){ return { type: "topic", item: item }; });

    var labResults = flatLabSections.filter(function(x){
      return sectionSidebarLabel(x.section).toLowerCase().indexOf(q) !== -1 ||
             ("lab assignment " + x.assignment.num).indexOf(q) !== -1 ||
             x.assignment.subtitle.toLowerCase().indexOf(q) !== -1;
    }).map(function(item){ return { type: "lab", item: item }; });

    var results = topicResults.concat(labResults).slice(0, 20);
    currentResults = results;
    searchActiveIndex = -1;
    if(!results.length){
      searchResults.innerHTML = '<div class="search-empty">No topics found for “' + escapeHtml(q) + '”</div>';
    } else {
      searchResults.innerHTML = results.map(function(result, i){
        if(result.type === "topic"){
          var item = result.item;
          return '<div class="search-result" data-i="' + i + '">' +
            '<span class="sr-title">' + escapeHtml(item.topic.title) + '</span>' +
            '<span class="sr-meta">' + escapeHtml(lecLabel(item.lecture)) + ' · ' + escapeHtml(item.lecture.title) + '</span>' +
          '</div>';
        } else {
          var li = result.item;
          return '<div class="search-result" data-i="' + i + '">' +
            '<span class="sr-title">' + escapeHtml(sectionSidebarLabel(li.section)) + '</span>' +
            '<span class="sr-meta">Lab Assignment ' + li.assignment.num + ' · ' + escapeHtml(li.assignment.subtitle) + '</span>' +
          '</div>';
        }
      }).join("");
    }
    searchResults.classList.remove("hidden");
  }

  searchInput.addEventListener("input", function(){ runSearch(searchInput.value); });
  searchInput.addEventListener("focus", function(){ if(searchInput.value.trim()) runSearch(searchInput.value); });
  searchResults.addEventListener("click", function(e){
    var el = e.target.closest(".search-result");
    if(!el) return;
    goToResult(parseInt(el.dataset.i, 10));
  });
  searchInput.addEventListener("keydown", function(e){
    if(e.key === "Escape"){ searchResults.classList.add("hidden"); searchInput.blur(); return; }
    if(!currentResults.length) return;
    if(e.key === "ArrowDown"){
      e.preventDefault();
      searchActiveIndex = Math.min(searchActiveIndex + 1, currentResults.length - 1);
      highlightSearch();
    } else if(e.key === "ArrowUp"){
      e.preventDefault();
      searchActiveIndex = Math.max(searchActiveIndex - 1, 0);
      highlightSearch();
    } else if(e.key === "Enter"){
      e.preventDefault();
      goToResult(searchActiveIndex >= 0 ? searchActiveIndex : 0);
    }
  });
  function highlightSearch(){
    Array.prototype.forEach.call(searchResults.querySelectorAll(".search-result"), function(el, i){
      el.classList.toggle("active", i === searchActiveIndex);
    });
  }
  function goToResult(i){
    var result = currentResults[i];
    if(!result) return;
    if(result.type === "topic"){
      location.hash = "#/lecture/" + result.item.lecture.num + "/" + result.item.topic.id;
    } else {
      location.hash = "#/lab/" + result.item.assignment.num + "/" + result.item.section.id;
    }
    searchInput.value = ""; searchResults.classList.add("hidden");
  }
  document.addEventListener("click", function(e){
    if(!e.target.closest(".search-wrap")) searchResults.classList.add("hidden");
  });
  document.addEventListener("keydown", function(e){
    if((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k"){
      e.preventDefault(); searchInput.focus();
    }
  });

  // ---------------- Helpers ----------------
  function escapeHtml(s){
    return String(s).replace(/[&<>"']/g, function(c){
      return { "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;" }[c];
    });
  }

  var SECTION_ICONS = ["🎓", "💬", "🇮🇳"];

  // ---------------- Views ----------------
  var content = document.getElementById("content");

  function renderHome(){
    document.title = "ES532 · Introduction to Deep Learning — Lecture Notes";
    var html = '<div class="home-hero">' +
      '<h1>ES532 — Introduction to Deep Learning</h1>' +
      '<p>Complete lecture notes, topic by topic. Every concept is explained three ways — precise Technical language, plain Simple English, and beginner-friendly Hinglish — so it works whether you already know some ML or you\'re starting from absolute zero.</p>' +
      '<div class="home-stats">' +
        '<div class="home-stat"><b>' + LECTURES.length + '</b><span>Lectures</span></div>' +
        '<div class="home-stat"><b>' + totalTopics + '</b><span>Topics</span></div>' +
        '<div class="home-stat"><b>3</b><span>Explanation styles / topic</span></div>' +
      '</div>' +
    '</div>';

    html += '<div class="lecture-cards">';
    LECTURES.forEach(function(lec){
      html += '<a class="lecture-card" href="#/lecture/' + lec.num + '">' +
        '<span class="lc-num">' + escapeHtml(lecLabel(lec)) + '</span>' +
        '<h3>' + escapeHtml(lec.title) + '</h3>' +
        '<p>' + lec.topics.length + ' topics' + (lec.subtitle ? ' · ' + escapeHtml(lec.subtitle) : '') + '</p>' +
      '</a>';
    });
    html += '</div>';

    if(LAB_ASSIGNMENTS.length){
      html += '<div class="home-hero" style="border-bottom:none;padding-bottom:0;margin-bottom:20px;">' +
        '<h1 style="font-size:22px;">Lab Assignments</h1>' +
        '<p style="margin-bottom:0;">Full, beginner-friendly, line-by-line Python solutions — same dataset carried across assignments so you can see how a real cleaning → visualization → scaling pipeline connects.</p>' +
      '</div>';
      html += '<div class="lecture-cards">';
      LAB_ASSIGNMENTS.forEach(function(lab){
        var qCount = lab.sections.filter(function(s){ return s.kind === "question"; }).length;
        html += '<a class="lecture-card lab-card" href="#/lab/' + lab.num + '">' +
          '<span class="lc-num">Lab Assignment ' + lab.num + '</span>' +
          '<h3>' + escapeHtml(lab.subtitle || ("Lab Assignment " + lab.num)) + '</h3>' +
          '<p>' + qCount + ' questions · dataset: ' + escapeHtml(lab.dataset) + '</p>' +
        '</a>';
      });
      html += '</div>';
    }

    html += '<div class="footer-note">Built from the course PDFs, lecture by lecture. Use the search bar or sidebar to jump straight to any topic.</div>';

    content.innerHTML = html;
    window.scrollTo(0,0);
  }

  function renderLecture(lec){
    document.title = lecLabel(lec) + " · " + lec.title + " — ES532 Notes";
    var html = '<div class="crumbs"><a href="#/">Home</a><span class="crumb-sep">/</span><span>' + escapeHtml(lecLabel(lec)) + '</span></div>';
    html += '<div class="lecture-overview-head">' +
      '<h1>' + escapeHtml(lecLabel(lec)) + ' — ' + escapeHtml(lec.title) + '</h1>';
    if(lec.subtitle) html += '<div class="subtitle">' + escapeHtml(lec.subtitle) + '</div>';
    if(lec.source_pdf) html += '<div class="pdf-pill">📄 ' + escapeHtml(lec.source_pdf) + '</div>';
    html += '</div>';

    html += '<div class="topic-grid">';
    lec.topics.forEach(function(t, i){
      html += '<a class="topic-grid-item" href="#/lecture/' + lec.num + '/' + t.id + '">' +
        '<span class="topic-grid-num">' + String(i+1).padStart(2,"0") + '</span>' +
        '<span class="topic-grid-title">' + escapeHtml(t.title) + '</span>' +
      '</a>';
    });
    html += '</div>';

    content.innerHTML = html;
    window.scrollTo(0,0);
  }

  function renderTopic(lec, topic){
    document.title = topic.title + " · " + lecLabel(lec) + " — ES532 Notes";
    var idx = lec.topics.indexOf(topic);
    var prev = idx > 0 ? lec.topics[idx-1] : null;
    var next = idx < lec.topics.length - 1 ? lec.topics[idx+1] : null;

    var html = '<div class="crumbs"><a href="#/">Home</a><span class="crumb-sep">/</span>' +
      '<a href="#/lecture/' + lec.num + '">' + escapeHtml(lecLabel(lec)) + '</a><span class="crumb-sep">/</span>' +
      '<span>' + escapeHtml(topic.title) + '</span></div>';

    html += '<div class="topic-head"><h1>' + escapeHtml(topic.title) + '</h1>';
    if(topic.source) html += '<div class="topic-source">' + escapeHtml(topic.source) + '</div>';
    html += '</div>';

    var diagrams = DIAGRAMS[lec.num + "-" + topic.id];
    if(diagrams && diagrams.length){
      html += '<div class="diagram-block">';
      diagrams.forEach(function(d){
        html += '<figure class="diagram-card">' + d.svg + '<figcaption>' + escapeHtml(d.caption) + '</figcaption></figure>';
      });
      html += '</div>';
    }

    if(topic.sections && topic.sections.length){
      html += '<div class="tabbar" role="tablist">';
      topic.sections.forEach(function(sec, i){
        html += '<button class="tab-btn' + (i===0 ? " active" : "") + '" data-tab="' + i + '">' +
          (SECTION_ICONS[i] || "") + ' ' + escapeHtml(shortLabel(sec.heading)) + '</button>';
      });
      html += '</div>';

      topic.sections.forEach(function(sec, i){
        html += '<div class="tab-panel' + (i===0 ? " active" : "") + '" data-panel="' + i + '">' +
          '<div class="prose">' + sec.html + '</div>' +
        '</div>';
      });
    }

    html += '<div class="topic-pager">';
    if(prev){
      html += '<a class="pager-link prev" href="#/lecture/' + lec.num + '/' + prev.id + '">' +
        '<span class="pager-label">← Previous</span><span class="pager-title">' + escapeHtml(prev.title) + '</span></a>';
    } else { html += '<span></span>'; }
    if(next){
      html += '<a class="pager-link next" href="#/lecture/' + lec.num + '/' + next.id + '">' +
        '<span class="pager-label">Next →</span><span class="pager-title">' + escapeHtml(next.title) + '</span></a>';
    } else { html += '<span></span>'; }
    html += '</div>';

    content.innerHTML = html;
    window.scrollTo(0,0);

    // tabs
    var tabBtns = content.querySelectorAll(".tab-btn");
    var panels = content.querySelectorAll(".tab-panel");
    tabBtns.forEach(function(btn){
      btn.addEventListener("click", function(){
        tabBtns.forEach(function(b){ b.classList.remove("active"); });
        panels.forEach(function(p){ p.classList.remove("active"); });
        btn.classList.add("active");
        content.querySelector('.tab-panel[data-panel="' + btn.dataset.tab + '"]').classList.add("active");
      });
    });

    // cross-ref buttons
    content.querySelectorAll(".xref").forEach(function(btn){
      btn.addEventListener("click", function(){
        location.hash = "#/lecture/" + btn.dataset.lec + "/" + btn.dataset.id;
      });
    });
  }

  // ---------------- Lab Assignment views ----------------

  function renderIntroHtml(introText){
    // The intro is the assignment script's own top module docstring - plain
    // text, not markdown. We turn it into readable HTML with a small set of
    // heuristics: a line immediately followed by a line of only "-"
    // characters is a heading; blank lines separate paragraphs; lines
    // starting with a digit+"." or "-" render as a list item.
    var lines = introText.split("\n");
    var html = "";
    var i = 0;
    var paragraphBuffer = [];
    var listBuffer = [];

    function flushParagraph(){
      if(paragraphBuffer.length){
        html += "<p>" + escapeHtml(paragraphBuffer.join(" ")) + "</p>";
        paragraphBuffer = [];
      }
    }
    function flushList(){
      if(listBuffer.length){
        html += "<ul>" + listBuffer.map(function(li){ return "<li>" + escapeHtml(li) + "</li>"; }).join("") + "</ul>";
        listBuffer = [];
      }
    }

    while(i < lines.length){
      var line = lines[i];
      var next = lines[i+1] || "";
      var trimmed = line.trim();

      if(/^={3,}$/.test(trimmed)){ i++; continue; } // skip decorative ==== rules
      if(/^-{3,}$/.test(next.trim()) && trimmed){
        flushParagraph(); flushList();
        html += "<h3>" + escapeHtml(trimmed) + "</h3>";
        i += 2; continue;
      }
      if(!trimmed){
        flushParagraph(); flushList();
        i++; continue;
      }
      var listMatch = trimmed.match(/^(?:[-*]|\d+\.)\s+(.*)$/);
      if(listMatch){
        flushParagraph();
        listBuffer.push(listMatch[1]);
        i++; continue;
      }
      flushList();
      paragraphBuffer.push(trimmed);
      i++;
    }
    flushParagraph(); flushList();
    return html;
  }

  var LAB_STYLES = ["technical", "simple", "hinglish"];
  var LAB_STYLE_LABELS = { technical: "🎓 Technical", simple: "💬 Simple English", hinglish: "🇮🇳 Hinglish" };
  var labStyle = localStorage.getItem("dl-lab-style") || "technical";

  function renderChunksHtml(chunks, style){
    return chunks.map(function(chunk){
      if(chunk.type === "explanation"){
        var text = chunk[style] || chunk.simple || chunk.text || "";
        var paras = text.split("\n\n").map(function(p){
          var headingMatch = p.match(/^@@(.+)@@$/);
          if(headingMatch) return "<p class=\"mini-heading\">" + escapeHtml(headingMatch[1]) + "</p>";
          return "<p>" + escapeHtml(p) + "</p>";
        }).join("");
        return '<div class="explanation-card">' + paras + '</div>';
      } else {
        return '<pre class="code-block"><code class="language-python">' + escapeHtml(chunk.text) + '</code></pre>';
      }
    }).join("");
  }

  function renderLabStyleTabs(){
    return '<div class="tabbar lab-style-tabbar" role="tablist">' +
      LAB_STYLES.map(function(s){
        return '<button class="tab-btn' + (s === labStyle ? " active" : "") + '" data-style="' + s + '">' +
          LAB_STYLE_LABELS[s] + '</button>';
      }).join("") +
    '</div>';
  }

  function renderOutputHtml(section){
    if(!section.output || !section.output.trim()) return "";
    return '<div class="output-panel">' +
      '<div class="output-panel-head">▸ Sample Output (captured from a real run on the Titanic dataset)</div>' +
      '<pre class="output-panel-body">' + escapeHtml(section.output) + '</pre>' +
    '</div>';
  }

  function renderPlotsHtml(section){
    if(!section.plots || !section.plots.length) return "";
    return '<div class="plot-gallery">' + section.plots.map(function(p){
      var caption = p.filename.replace(/\.png$/, "").replace(/^\d+[a-z]?_/, "").replace(/_/g, " ");
      return '<figure class="plot-card">' +
        '<img src="' + p.data_uri + '" alt="' + escapeHtml(caption) + '" loading="lazy" />' +
        '<figcaption>' + escapeHtml(caption) + '</figcaption>' +
      '</figure>';
    }).join("") + '</div>';
  }

  function highlightCodeBlocks(){
    if(window.hljs){
      content.querySelectorAll("pre.code-block code").forEach(function(el){
        window.hljs.highlightElement(el);
      });
    }
  }

  function renderLabAssignment(lab){
    document.title = "Lab Assignment " + lab.num + " — ES532 Notes";
    var html = '<div class="crumbs"><a href="#/">Home</a><span class="crumb-sep">/</span><span>Lab Assignment ' + lab.num + '</span></div>';
    html += '<div class="lecture-overview-head">' +
      '<h1>Lab Assignment ' + lab.num + ' — ' + escapeHtml(lab.subtitle) + '</h1>' +
      '<div class="pdf-pill">📊 Dataset used: ' + escapeHtml(lab.dataset) + '</div>' +
    '</div>';

    html += '<div class="prose">' + renderIntroHtml(lab.intro) + '</div>';

    html += '<div class="topic-grid" style="margin-top:28px;">';
    lab.sections.forEach(function(s){
      html += '<a class="topic-grid-item" href="#/lab/' + lab.num + '/' + s.id + '">' +
        '<span class="topic-grid-num">' + (s.kind === "question" ? "Q" + s.number : (s.kind === "setup" ? "0" : "✓")) + '</span>' +
        '<span class="topic-grid-title">' + escapeHtml(sectionSidebarLabel(s)) + (s.kind === "question" ? " — " + escapeHtml(s.label) : "") + '</span>' +
      '</a>';
    });
    html += '</div>';

    content.innerHTML = html;
    window.scrollTo(0,0);
  }

  function renderLabSection(lab, section){
    document.title = sectionSidebarLabel(section) + " · Lab Assignment " + lab.num + " — ES532 Notes";
    var idx = lab.sections.indexOf(section);
    var prev = idx > 0 ? lab.sections[idx-1] : null;
    var next = idx < lab.sections.length - 1 ? lab.sections[idx+1] : null;

    var html = '<div class="crumbs"><a href="#/">Home</a><span class="crumb-sep">/</span>' +
      '<a href="#/lab/' + lab.num + '">Lab Assignment ' + lab.num + '</a><span class="crumb-sep">/</span>' +
      '<span>' + escapeHtml(sectionSidebarLabel(section)) + '</span></div>';

    html += '<div class="topic-head">';
    html += '<h1>' + escapeHtml(sectionSidebarLabel(section)) + '</h1>';
    html += '<div class="pdf-pill">📊 Dataset used: ' + escapeHtml(lab.dataset) + '</div>';
    html += '</div>';

    if(section.kind === "question"){
      html += '<blockquote class="lab-prompt"><strong>Assignment question:</strong> ' + escapeHtml(section.label) + '</blockquote>';
    }

    html += '<div class="run-bar">' +
      '<button class="run-btn" disabled title="Live in-browser execution is coming in a future update">▶ Run this code</button>' +
      '<span class="run-note">Live execution isn\'t wired up yet — below is the exact output captured from a real run of this code on the Titanic dataset.</span>' +
    '</div>';

    html += renderLabStyleTabs();
    html += '<div class="lab-chunks" id="labChunks">' + renderChunksHtml(section.chunks, labStyle) + '</div>';
    html += renderOutputHtml(section);
    html += renderPlotsHtml(section);

    html += '<div class="topic-pager">';
    if(prev){
      html += '<a class="pager-link prev" href="#/lab/' + lab.num + '/' + prev.id + '">' +
        '<span class="pager-label">← Previous</span><span class="pager-title">' + escapeHtml(sectionSidebarLabel(prev)) + '</span></a>';
    } else { html += '<span></span>'; }
    if(next){
      html += '<a class="pager-link next" href="#/lab/' + lab.num + '/' + next.id + '">' +
        '<span class="pager-label">Next →</span><span class="pager-title">' + escapeHtml(sectionSidebarLabel(next)) + '</span></a>';
    } else { html += '<span></span>'; }
    html += '</div>';

    content.innerHTML = html;
    window.scrollTo(0,0);
    highlightCodeBlocks();

    content.querySelectorAll(".lab-style-tabbar .tab-btn").forEach(function(btn){
      btn.addEventListener("click", function(){
        labStyle = btn.dataset.style;
        localStorage.setItem("dl-lab-style", labStyle);
        content.querySelectorAll(".lab-style-tabbar .tab-btn").forEach(function(b){
          b.classList.toggle("active", b === btn);
        });
        document.getElementById("labChunks").innerHTML = renderChunksHtml(section.chunks, labStyle);
        highlightCodeBlocks();
      });
    });
  }

  function shortLabel(heading){
    // "Hinglish Explanation (Beginner-Friendly)" -> "Hinglish"
    // "Simple English Explanation" -> "Simple English"
    // "Technical Explanation" -> "Technical"
    return heading.replace(/\s*Explanation.*$/i, "").trim() || heading;
  }

  // ---------------- Ask DL AI (chatbot) ----------------
  var chatMessages = []; // {role: "user"|"assistant"|"error", text: string}
  var chatResponseId = null;
  var chatBusy = false;
  var chatPassword = null;
  try { chatPassword = sessionStorage.getItem("dl-chat-pw") || null; } catch(e){ /* private mode etc. */ }
  var chatPwError = "";
  var chatGateChecking = false;

  // Auto password-verify-on-load disabled along with the rest of the chat
  // feature (see the disabled nav link and router branch above) — no need
  // to ping /api/chat on every page load while chat is off.
  // if(chatPassword){
  //   fetch("/api/chat", {
  //     method: "POST",
  //     headers: { "Content-Type": "application/json" },
  //     body: JSON.stringify({ password: chatPassword, verify_only: true }),
  //   }).then(function(res){
  //     if(!res.ok){
  //       chatPassword = null;
  //       try { sessionStorage.removeItem("dl-chat-pw"); } catch(e){ /* ignore */ }
  //       if((location.hash || "#/").indexOf("#/chat") === 0) renderChat();
  //     }
  //   }).catch(function(){ /* network hiccup: don't lock the user out over this */ });
  // }

  function mdInline(s){
    s = s.replace(/`([^`]+)`/g, '<code>$1</code>');
    s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    s = s.replace(/(^|[^*])\*([^*\n]+)\*(?!\*)/g, '$1<em>$2</em>');
    s = s.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
    return s;
  }

  function renderMarkdownLite(raw){
    var codeBlocks = [];
    var withoutCode = raw.replace(/```([a-zA-Z0-9_-]*)\n?([\s\S]*?)```/g, function(_, lang, code){
      codeBlocks.push('<pre class="code-block"><code class="language-' + (lang || "python") + '">' + escapeHtml(code.replace(/\n$/, "")) + '</code></pre>');
      return "\u0000CODEBLOCK" + (codeBlocks.length - 1) + "\u0000";
    });

    var lines = withoutCode.split("\n");
    var html = "";
    var listBuffer = [];
    var listType = null;
    var paraBuffer = [];

    function flushPara(){
      if(paraBuffer.length){
        html += "<p>" + mdInline(escapeHtml(paraBuffer.join(" "))) + "</p>";
        paraBuffer = [];
      }
    }
    function flushList(){
      if(listBuffer.length){
        var tag = listType === "ol" ? "ol" : "ul";
        html += "<" + tag + ">" + listBuffer.map(function(li){ return "<li>" + mdInline(escapeHtml(li)) + "</li>"; }).join("") + "</" + tag + ">";
        listBuffer = []; listType = null;
      }
    }

    lines.forEach(function(line){
      var trimmed = line.trim();
      var codeMatch = trimmed.match(/^\u0000CODEBLOCK(\d+)\u0000$/);
      if(codeMatch){
        flushPara(); flushList();
        html += codeBlocks[parseInt(codeMatch[1], 10)];
        return;
      }
      var h = trimmed.match(/^(#{1,4})\s+(.+)$/);
      if(h){
        flushPara(); flushList();
        var level = Math.min(h[1].length + 2, 5); // ## -> h4, ### -> h5 (keep visually subordinate to page h1/h2)
        html += "<h" + level + ">" + mdInline(escapeHtml(h[2])) + "</h" + level + ">";
        return;
      }
      var ol = trimmed.match(/^\d+\.\s+(.+)$/);
      var ul = trimmed.match(/^[-*]\s+(.+)$/);
      if(ol){
        flushPara();
        if(listType && listType !== "ol"){ flushList(); }
        listType = "ol"; listBuffer.push(ol[1]);
        return;
      }
      if(ul){
        flushPara();
        if(listType && listType !== "ul"){ flushList(); }
        listType = "ul"; listBuffer.push(ul[1]);
        return;
      }
      if(!trimmed){
        flushPara(); flushList();
        return;
      }
      flushList();
      paraBuffer.push(trimmed);
    });
    flushPara(); flushList();
    return html || "<p></p>";
  }

  function chatBubbleHtml(msg){
    if(msg.role === "user"){
      return '<div class="chat-msg chat-user"><div class="chat-bubble">' + escapeHtml(msg.text) + '</div></div>';
    }
    if(msg.role === "error"){
      return '<div class="chat-msg chat-assistant chat-error"><div class="chat-bubble"><strong>⚠ ' + escapeHtml(msg.text) + '</strong></div></div>';
    }
    return '<div class="chat-msg chat-assistant"><div class="chat-avatar">🤖</div><div class="chat-bubble">' + renderMarkdownLite(msg.text) + '</div></div>';
  }

  function renderChatPasswordGate(){
    document.title = "Ask DL AI · DL Notes";
    content.classList.add("content-chat");
    var html = '<div class="chat-head"><h1>🤖 Ask DL AI</h1>' +
      '<p>Enter the 6-digit access code to start chatting.</p></div>';
    html += '<div class="chat-panel chat-gate-panel">';
    html += '<form class="chat-gate-form" id="chatGateForm">' +
      '<input id="chatGateInput" type="password" inputmode="numeric" maxlength="6" autocomplete="off" placeholder="••••••" ' + (chatGateChecking ? "disabled" : "") + ' />' +
      (chatPwError ? '<div class="chat-gate-error">' + escapeHtml(chatPwError) + '</div>' : '') +
      '<button type="submit" class="chat-gate-btn" ' + (chatGateChecking ? "disabled" : "") + '>' + (chatGateChecking ? "Checking…" : "Unlock") + '</button>' +
    '</form>';
    html += '</div>';
    content.innerHTML = html;
    window.scrollTo(0, 0);

    var gateForm = document.getElementById("chatGateForm");
    var gateInput = document.getElementById("chatGateInput");
    if(!chatGateChecking) gateInput.focus();
    gateForm.addEventListener("submit", function(e){
      e.preventDefault();
      if(chatGateChecking) return;
      var val = gateInput.value.trim();
      if(!/^\d{6}$/.test(val)){
        chatPwError = "6-digit code daalo.";
        renderChat();
        return;
      }
      chatGateChecking = true;
      chatPwError = "";
      renderChat();

      fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password: val, verify_only: true }),
      })
        .then(function(res){ return { ok: res.ok, status: res.status }; })
        .then(function(result){
          chatGateChecking = false;
          if(!result.ok){
            chatPwError = "Galat code, dobara try karo.";
            renderChat();
            return;
          }
          chatPassword = val;
          try { sessionStorage.setItem("dl-chat-pw", val); } catch(e){ /* ignore */ }
          renderChat();
        })
        .catch(function(){
          chatGateChecking = false;
          chatPwError = "Verify nahi ho paaya, connection check karo aur dobara try karo.";
          renderChat();
        });
    });
  }

  function renderChat(){
    if(!chatPassword){
      renderChatPasswordGate();
      return;
    }
    document.title = "Ask DL AI · DL Notes";
    content.classList.add("content-chat");
    var html = '<div class="chat-head"><h1>🤖 Ask DL AI</h1>' +
      '<p>Your DL study assistant — grounded in these exact lecture notes and lab assignments, ' +
      'plus live web research for extra depth. Ask in English or Hinglish, about anything from any lecture or lab.</p></div>';

    html += '<div class="chat-panel">';
    html += '<div class="chat-thread" id="chatThread">';
    if(!chatMessages.length){
      html += '<div class="chat-empty">Try: <em>"Lecture 6 mein kya kya hai?"</em>, ' +
        '<em>"Explain PCA simply"</em>, or <em>"What did we do in Lab Assignment 2, Question 3?"</em></div>';
    } else {
      html += chatMessages.map(chatBubbleHtml).join("");
    }
    if(chatBusy){
      html += '<div class="chat-msg chat-assistant"><div class="chat-avatar">🤖</div><div class="chat-bubble chat-typing"><span></span><span></span><span></span></div></div>';
    }
    html += '</div>';

    html += '<form class="chat-inputbar" id="chatForm">' +
      '<textarea id="chatInput" rows="1" placeholder="Ask about any lecture or lab assignment…" ' + (chatBusy ? "disabled" : "") + '></textarea>' +
      '<button type="submit" class="chat-send-btn" ' + (chatBusy ? "disabled" : "") + '>➤</button>' +
    '</form>';
    html += '<div class="chat-disclaimer">AI-generated — always double-check against the actual notes for exam prep. Requires an OpenAI key configured server-side.</div>';
    html += '</div>';

    content.innerHTML = html;
    var thread = document.getElementById("chatThread");
    thread.scrollTop = thread.scrollHeight;
    window.scrollTo(0, 0);

    var form = document.getElementById("chatForm");
    var input = document.getElementById("chatInput");
    input.addEventListener("keydown", function(e){
      if(e.key === "Enter" && !e.shiftKey){
        e.preventDefault();
        form.requestSubmit();
      }
    });
    input.addEventListener("input", function(){
      input.style.height = "auto";
      input.style.height = Math.min(input.scrollHeight, 160) + "px";
    });
    if(!chatBusy) input.focus();

    form.addEventListener("submit", function(e){
      e.preventDefault();
      var text = input.value.trim();
      if(!text || chatBusy) return;
      sendChatMessage(text);
    });
  }

  function sendChatMessage(text){
    chatMessages.push({ role: "user", text: text });
    chatBusy = true;
    renderChat();

    fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text, previous_response_id: chatResponseId, password: chatPassword }),
    })
      .then(function(res){ return res.json().then(function(data){ return { ok: res.ok, status: res.status, data: data }; }); })
      .then(function(result){
        chatBusy = false;
        if(result.status === 401){
          chatMessages.pop(); // drop the just-sent user message, it never got answered
          chatPassword = null;
          chatResponseId = null;
          chatPwError = "Galat code, dobara try karo.";
          try { sessionStorage.removeItem("dl-chat-pw"); } catch(e){ /* ignore */ }
          renderChat();
          return;
        }
        if(!result.ok){
          chatMessages.push({ role: "error", text: (result.data && result.data.error) || "Something went wrong." });
        } else {
          chatResponseId = result.data.response_id || chatResponseId;
          chatMessages.push({ role: "assistant", text: result.data.reply || "(no reply)" });
        }
        renderChat();
        highlightCodeBlocks();
      })
      .catch(function(){
        chatBusy = false;
        chatMessages.push({ role: "error", text: "Couldn't reach the AI backend. Check your connection and try again." });
        renderChat();
      });
  }

  function render404(){
    content.innerHTML = '<div class="crumbs"><a href="#/">Home</a></div>' +
      '<div class="home-hero"><h1>Not found</h1><p>That lecture or topic doesn\'t exist. Head back to the homepage.</p></div>';
  }

  // ---------------- Router ----------------
  function route(){
    var hash = location.hash || "#/";
    var parts = hash.replace(/^#\//, "").split("/").filter(Boolean);
    content.classList.remove("content-chat");

    if(parts[0] === "lecture" && parts[1]){
      var lecNum = parseInt(parts[1], 10);
      var lec = byLecture[lecNum];
      if(!lec){ render404(); renderSidebar(); return; }
      if(parts[2]){
        var key = lecNum + "-" + parts[2];
        var entry = byTopicKey[key];
        if(!entry){ render404(); renderSidebar(lecNum); return; }
        renderTopic(entry.lecture, entry.topic);
        renderSidebar(lecNum, parts[2]);
      } else {
        renderLecture(lec);
        renderSidebar(lecNum, null);
      }
    } else if(parts[0] === "lab" && parts[1]){
      var labNum = parseInt(parts[1], 10);
      var lab = byLab[labNum];
      if(!lab){ render404(); renderSidebar(); return; }
      if(parts[2]){
        var labKey = labNum + "-" + parts[2];
        var labEntry = byLabSectionKey[labKey];
        if(!labEntry){ render404(); renderSidebar(null, null, labNum); return; }
        renderLabSection(labEntry.assignment, labEntry.section);
        renderSidebar(null, null, labNum, parts[2]);
      } else {
        renderLabAssignment(lab);
        renderSidebar(null, null, labNum, null);
      }
    // "chat" route disabled for now, matching the nav link above — falls
    // through to renderHome() instead. Restore this branch (and the nav
    // link at the top of renderSidebar) to bring the chatbot back.
    // } else if(parts[0] === "chat"){
    //   renderChat();
    //   renderSidebar(null, null, null, null, true);
    } else {
      renderHome();
      renderSidebar(null, null);
    }
  }

  window.addEventListener("hashchange", route);
  route();
})();
