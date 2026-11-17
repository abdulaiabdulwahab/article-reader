(() => {
  const search = document.getElementById('article-search');
  if (!search) return;
  const cards = [...document.querySelectorAll('.story-card')];
  const empty = document.getElementById('no-results');
  const update = () => {
    const query = search.value.trim().toLowerCase();
    let visible = 0;
    cards.forEach(card => { const matches = (card.dataset.searchable || '').includes(query); card.hidden = !matches; if (matches) visible++; });
    if (empty) empty.hidden = visible !== 0;
  };
  search.addEventListener('input', update);
})();
