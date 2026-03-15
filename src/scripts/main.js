/* ═══════ Sidebar Navigation ═══════ */
// Tab switching via sidebar links
document.querySelectorAll('.sidebar-link').forEach(link => {
  link.addEventListener('click', () => {
    const tabId = link.dataset.tab;
    if (!tabId) return;
    // Update sidebar active states
    document.querySelectorAll('.sidebar-link').forEach(l => l.classList.remove('active'));
    link.classList.add('active');
    // Switch tab content
    document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
    const target = document.getElementById('tab-' + tabId);
    if (target) target.classList.add('active');
    // Scroll to top of content — target the active tab, not window top
    if (target) {
      target.scrollIntoView({ behavior: 'instant', block: 'start' });
    } else {
      window.scrollTo({ top: 0, behavior: 'instant' });
    }
    // Close mobile sidebar
    closeSidebar();
  });
});

// Sidebar accordion
document.querySelectorAll('.sidebar-volume-title').forEach(btn => {
  btn.addEventListener('click', () => {
    const volume = btn.closest('.sidebar-volume');
    if (!volume) return;
    document.querySelectorAll('.sidebar-volume').forEach(v => {
      if (v !== volume) v.classList.remove('open');
    });
    volume.classList.toggle('open');
  });
});

// Mobile sidebar management
const sidebar = document.getElementById('codexSidebar');
const sidebarOverlay = document.getElementById('sidebarOverlay');
const sidebarToggle = document.getElementById('sidebarToggle');

function closeSidebar() {
  sidebar?.classList.remove('open');
  sidebarOverlay?.classList.remove('visible');
}

sidebarToggle?.addEventListener('click', () => {
  sidebar?.classList.toggle('open');
  sidebarOverlay?.classList.toggle('visible');
});

sidebarOverlay?.addEventListener('click', closeSidebar);

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && sidebar?.classList.contains('open')) {
    closeSidebar();
    sidebarToggle?.focus();
  }
});

/* ═══════ Scroll to Top ═══════ */
const scrollTopBtn = document.getElementById('scrollTopBtn');
window.addEventListener('scroll', () => {
  if (window.scrollY > 400) {
    scrollTopBtn?.classList.add('visible');
  } else {
    scrollTopBtn?.classList.remove('visible');
  }
});
scrollTopBtn?.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

function toggleMove(el) { el.classList.toggle('open'); }

/* ═══════ Generic Panel Switch Utility ═══════ */
function switchPanel(id, evt, btnSelector, btnActiveClass, panelSelector, idPrefix) {
  document.querySelectorAll(btnSelector).forEach(b => b.classList.remove(btnActiveClass));
  document.querySelectorAll(panelSelector).forEach(p => p.classList.remove('active-panel'));
  const target = document.getElementById(idPrefix + id);
  if (target) target.classList.add('active-panel');
  if (evt && evt.currentTarget) evt.currentTarget.classList.add(btnActiveClass);
}

function switchCompanion(id, evt) {
  switchPanel(id, evt, '.companion-btn', 'active-companion', '.companion-panel', 'panel-');
}

function switchFamily(id, evt) {
  switchPanel(id, evt, '.family-btn', 'active-family', '.family-panel', 'familypanel-');
}

function switchArsenal(id, evt) {
  switchPanel(id, evt, '#tab-arsenal > .arsenal-selector .arsenal-btn', 'active-arsenal', '.arsenal-panel', 'arsenal-');
}

function switchSynergy(id, evt) {
  switchPanel(id, evt, '#tab-synergy .arsenal-btn', 'active-arsenal', '.synergy-panel', 'synergy-');
}

function switchReputation(id, evt) {
  switchPanel(id, evt, '#tab-reputation .arsenal-btn', 'active-arsenal', '.reputation-panel', 'reputation-');
}

function switchStars(id, evt) {
  switchPanel(id, evt, '#tab-stars .arsenal-btn', 'active-arsenal', '.stars-panel', 'stars-');
}

function switchStatus(id, evt) {
  switchPanel(id, evt, '#tab-statusboard .status-board-btn', 'active-status', '.status-panel', 'status-');
}

function switchVessel(id, evt) {
  switchPanel(id, evt, '#tab-vessel .arsenal-btn', 'active-arsenal', '.vessel-panel', 'vessel-');
}

function switchArmory(id, evt) {
  switchPanel(id, evt, '#tab-armory .arsenal-btn', 'active-arsenal', '.armory-panel', 'armory-');
}

function switchJournal(id, evt) {
  switchPanel(id, evt, '#tab-journal .arsenal-btn', 'active-arsenal', '.journal-panel', 'journal-');
}

function switchWatch(id, evt) {
  switchPanel(id, evt, '#tab-watch .arsenal-btn', 'active-arsenal', '.watch-panel', 'watch-');
}

function switchLantern(id, evt) {
  switchPanel(id, evt, '#tab-lantern .arsenal-btn', 'active-arsenal', '.lantern-panel', 'lantern-');
}

function switchMartial(id, evt) {
  switchPanel(id, evt, '#tab-martial .companion-btn', 'active-companion', '.martial-panel', 'panel-');
}

function switchAuxiliary(id, evt) {
  switchPanel(id, evt, '#tab-auxiliary .companion-btn', 'active-companion', '.auxiliary-panel', 'aux-');
}

function switchAwakening(id, evt) {
  switchPanel(id, evt, '.awakening-nav .sub-btn', 'active-arsenal', '.awakening-panel', 'awakening-');
}

function switchInvestigation(id, evt) {
  switchPanel(id, evt, '#tab-investigations .arsenal-btn', 'active-arsenal', '.investigation-panel', 'investigation-');
}

function switchInvestigation2(id, evt) {
  switchPanel(id, evt, '.inv2-nav .arsenal-btn', 'active-arsenal', '.inv2-panel', 'inv2-');
}

function switchInvestigation3(id, evt) {
  switchPanel(id, evt, '.inv3-nav .arsenal-btn', 'active-arsenal', '.inv3-panel', 'inv3-');
}

function switchInvestigation4(id, evt) {
  switchPanel(id, evt, '.inv4-nav .arsenal-btn', 'active-arsenal', '.inv4-panel', 'inv4-');
}

function switchInvestigation5(id, evt) {
  switchPanel(id, evt, '.inv5-nav .arsenal-btn', 'active-arsenal', '.inv5-panel', 'inv5-');
}

function switchTraining(id, evt) {
  switchPanel(id, evt, '#tab-training .arsenal-btn', 'active-arsenal', '.training-panel', 'training-');
}

function switchMission(id, evt) {
  switchPanel(id, evt, '#tab-missions .arsenal-btn', 'active-arsenal', '.mission-panel', 'mission-');
}

function switchWayfarers(id, evt) {
  switchPanel(id, evt, '#tab-wayfarers .companion-btn', 'active-companion', '.wayfarers-panel', 'wayfarers-');
}

function switchTranscendence(id, evt) {
  switchPanel(id, evt, '#tab-transcendence .transcendence-btn', 'active-transcendence', '.transcendence-panel', 'trans-');
}

function toggleAccordionCard(header) {
  var card = header.parentElement;
  card.classList.toggle('collapsed');
}

/* ═══════ Cross-Link Navigation ═══════ */
document.addEventListener('click', function(e) {
  var link = e.target.closest('.xref[data-tab]');
  if (!link) return;
  e.preventDefault();
  var tabId = link.getAttribute('data-tab');
  var panelId = link.getAttribute('data-panel');
  var targetTab = document.getElementById('tab-' + tabId);
  if (!targetTab) return;
  document.querySelectorAll('.tab-content').forEach(function(t) { t.classList.remove('active'); });
  targetTab.classList.add('active');
  document.querySelectorAll('.sidebar-link').forEach(function(s) { s.classList.remove('active'); });
  var sidebarLink = document.querySelector('.sidebar-link[data-tab="' + tabId + '"]');
  if (sidebarLink) sidebarLink.classList.add('active');
  if (panelId) {
    var panel = document.getElementById(panelId);
    if (panel) {
      var siblings = panel.parentElement.querySelectorAll('[class*="-panel"]');
      siblings.forEach(function(s) { s.classList.remove('active-panel'); });
      panel.classList.add('active-panel');
    }
  }
  targetTab.scrollIntoView({ behavior: 'smooth', block: 'start' });
  closeSidebar();
});

/* ═══════ Hex Particles ═══════ */
const container = document.getElementById('hexParticles');
if (container) {
  for (let i = 0; i < 20; i++) {
    const p = document.createElement('div');
    p.className = 'hex-particle';
    p.style.left = Math.random() * 100 + '%';
    p.style.animationDuration = (15 + Math.random() * 25) + 's';
    p.style.animationDelay = (Math.random() * 20) + 's';
    const sz = (4 + Math.random() * 5) + 'px';
    p.style.width = sz; p.style.height = sz;
    container.appendChild(p);
  }
}
