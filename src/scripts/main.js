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

function switchCompanion(id) {
  document.querySelectorAll('.companion-btn').forEach(b => b.classList.remove('active-companion'));
  document.querySelectorAll('.companion-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('panel-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-companion');
}

function switchFamily(id) {
  document.querySelectorAll('.family-btn').forEach(b => b.classList.remove('active-family'));
  document.querySelectorAll('.family-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('familypanel-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-family');
}

function switchArsenal(id) {
  document.querySelectorAll('#tab-arsenal > .arsenal-selector .arsenal-btn').forEach(b => b.classList.remove('active-arsenal'));
  document.querySelectorAll('.arsenal-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('arsenal-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-arsenal');
}

function switchSynergy(id) {
  document.querySelectorAll('#tab-synergy .arsenal-btn').forEach(b => b.classList.remove('active-arsenal'));
  document.querySelectorAll('.synergy-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('synergy-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-arsenal');
}

function switchReputation(id) {
  document.querySelectorAll('#tab-reputation .arsenal-btn').forEach(b => b.classList.remove('active-arsenal'));
  document.querySelectorAll('.reputation-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('reputation-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-arsenal');
}

function switchStars(id) {
  document.querySelectorAll('#tab-stars .arsenal-btn').forEach(b => b.classList.remove('active-arsenal'));
  document.querySelectorAll('.stars-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('stars-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-arsenal');
}

function switchStatus(id) {
  document.querySelectorAll('#tab-statusboard .status-board-btn').forEach(b => b.classList.remove('active-status'));
  document.querySelectorAll('.status-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('status-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-status');
}

function switchVessel(id) {
  document.querySelectorAll('#tab-vessel .arsenal-btn').forEach(b => b.classList.remove('active-arsenal'));
  document.querySelectorAll('.vessel-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('vessel-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-arsenal');
}

function switchArmory(id) {
  document.querySelectorAll('#tab-armory .arsenal-btn').forEach(b => b.classList.remove('active-arsenal'));
  document.querySelectorAll('.armory-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('armory-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-arsenal');
}

function switchJournal(id) {
  document.querySelectorAll('#tab-journal .arsenal-btn').forEach(b => b.classList.remove('active-arsenal'));
  document.querySelectorAll('.journal-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('journal-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-arsenal');
}

function switchWatch(id) {
  document.querySelectorAll('#tab-watch .arsenal-btn').forEach(b => b.classList.remove('active-arsenal'));
  document.querySelectorAll('.watch-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('watch-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-arsenal');
}

function switchLantern(id) {
  document.querySelectorAll('#tab-lantern .arsenal-btn').forEach(b => b.classList.remove('active-arsenal'));
  document.querySelectorAll('.lantern-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('lantern-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-arsenal');
}

function switchMartial(id) {
  document.querySelectorAll('#tab-martial .companion-btn').forEach(b => b.classList.remove('active-companion'));
  document.querySelectorAll('.martial-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('panel-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-companion');
}

function switchAuxiliary(id) {
  document.querySelectorAll('#tab-auxiliary .companion-btn').forEach(b => b.classList.remove('active-companion'));
  document.querySelectorAll('.auxiliary-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('aux-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-companion');
}

function switchTranscendence(id) {
  document.querySelectorAll('#tab-transcendence .transcendence-btn').forEach(b => b.classList.remove('active-transcendence'));
  document.querySelectorAll('.transcendence-panel').forEach(p => p.classList.remove('active-panel'));
  document.getElementById('trans-' + id).classList.add('active-panel');
  event.currentTarget.classList.add('active-transcendence');
}

function toggleAccordionCard(header) {
  var card = header.parentElement;
  card.classList.toggle('collapsed');
}
const container = document.getElementById('hexParticles');
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