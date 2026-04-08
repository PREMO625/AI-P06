const state = {
  selectedSymptoms: new Set(),
  duration: '1-2 days',
};

const el = {
  symptoms: document.getElementById('symptoms'),
  durations: document.getElementById('durations'),
  age: document.getElementById('age'),
  painScale: document.getElementById('painScale'),
  ageValue: document.getElementById('ageValue'),
  painValue: document.getElementById('painValue'),
  runBtn: document.getElementById('runBtn'),
  clearBtn: document.getElementById('clearBtn'),
  triage: document.getElementById('triage'),
  diagnosis: document.getElementById('diagnosis'),
  carePlan: document.getElementById('carePlan'),
  reasoning: document.getElementById('reasoning'),
};

function escapeHtml(text) {
  return text
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;');
}

function markdownishToHtml(text) {
  if (!text) return '';
  const lines = text.split('\n');
  let html = '';
  let inList = false;

  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed) {
      if (inList) {
        html += '</ul>';
        inList = false;
      }
      continue;
    }

    if (trimmed.startsWith('### ')) {
      if (inList) {
        html += '</ul>';
        inList = false;
      }
      html += `<h4>${escapeHtml(trimmed.slice(4))}</h4>`;
      continue;
    }

    if (trimmed.startsWith('- ')) {
      if (!inList) {
        html += '<ul>';
        inList = true;
      }
      const li = escapeHtml(trimmed.slice(2)).replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
      html += `<li>${li}</li>`;
      continue;
    }

    if (inList) {
      html += '</ul>';
      inList = false;
    }

    const p = escapeHtml(trimmed).replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    html += `<p>${p}</p>`;
  }

  if (inList) html += '</ul>';
  return html;
}

function setResults(result) {
  el.triage.textContent = result.triage;
  el.diagnosis.innerHTML = markdownishToHtml(result.diagnosis);
  el.carePlan.innerHTML = markdownishToHtml(result.care_plan);
  el.reasoning.innerHTML = markdownishToHtml(result.reasoning);
}

function renderChips(container, values, onToggle, isActiveFn) {
  container.innerHTML = '';
  values.forEach((value) => {
    const chip = document.createElement('button');
    chip.type = 'button';
    chip.className = `chip${isActiveFn(value) ? ' active' : ''}`;
    chip.textContent = value;
    chip.addEventListener('click', () => {
      onToggle(value);
      chip.classList.toggle('active', isActiveFn(value));
    });
    container.appendChild(chip);
  });
}

function renderSymptoms(symptoms) {
  renderChips(
    el.symptoms,
    symptoms,
    (symptom) => {
      if (state.selectedSymptoms.has(symptom)) {
        state.selectedSymptoms.delete(symptom);
      } else {
        state.selectedSymptoms.add(symptom);
      }
    },
    (symptom) => state.selectedSymptoms.has(symptom)
  );
}

function renderDurations(durations) {
  renderChips(
    el.durations,
    durations,
    (duration) => {
      state.duration = duration;
      renderDurations(durations);
    },
    (duration) => duration === state.duration
  );
}

async function loadMeta() {
  const response = await fetch('/api/meta');
  if (!response.ok) throw new Error('Failed to load symptom catalog');

  const data = await response.json();
  renderSymptoms(data.symptoms);
  renderDurations(data.durations);
}

function resetForm() {
  state.selectedSymptoms.clear();
  state.duration = '1-2 days';
  el.age.value = '30';
  el.painScale.value = '3';
  el.ageValue.textContent = '30';
  el.painValue.textContent = '3';
  el.triage.textContent = 'Run diagnosis to see triage classification';
  el.diagnosis.innerHTML = '';
  el.carePlan.innerHTML = '';
  el.reasoning.innerHTML = '';
  loadMeta().catch(() => {});
}

async function runDiagnosis() {
  const payload = {
    symptoms: Array.from(state.selectedSymptoms),
    age: Number(el.age.value),
    pain_scale: Number(el.painScale.value),
    duration: state.duration,
  };

  const response = await fetch('/api/diagnose', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    const err = await response.text();
    throw new Error(err || 'Diagnosis failed');
  }

  const result = await response.json();
  setResults(result);
}

function bindEvents() {
  el.age.addEventListener('input', () => {
    el.ageValue.textContent = el.age.value;
  });

  el.painScale.addEventListener('input', () => {
    el.painValue.textContent = el.painScale.value;
  });

  el.runBtn.addEventListener('click', async () => {
    el.runBtn.disabled = true;
    el.runBtn.textContent = 'Diagnosing...';
    try {
      await runDiagnosis();
    } catch (error) {
      alert(error.message || 'Diagnosis failed');
    } finally {
      el.runBtn.disabled = false;
      el.runBtn.textContent = 'Run Expert Diagnosis';
    }
  });

  el.clearBtn.addEventListener('click', resetForm);
}

(async function init() {
  bindEvents();
  await loadMeta();
})();
