const state = {
  count: 0
};

const countEl = document.getElementById("count");

const increase = () => {
  state.count++;
  countEl.innerHTML = state.count;
};

