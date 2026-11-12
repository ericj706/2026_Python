"use strict";
const form = document.querySelector("#predict-form");
const dateInput = form.elements.namedItem("date");
const button = document.querySelector("#submit");
const errorBox = document.querySelector("#error");
const resultCard = document.querySelector("#result-card");

function updateDateSummary() {
  if (!dateInput.value) return;
  const date = new Date(`${dateInput.value}T12:00:00`);
  const month = date.getMonth() + 1;
  const season = [12, 1, 2].includes(month) ? "겨울" : month <= 5 ? "봄" : month <= 8 ? "여름" : "가을";
  document.querySelector("#date-summary").textContent = `${month}월 · ${["일", "월", "화", "수", "목", "금", "토"][date.getDay()]}요일 · ${season}`;
}
const today = new Date();
dateInput.value = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, "0")}-${String(today.getDate()).padStart(2, "0")}`;
dateInput.addEventListener("change", updateDateSummary);
updateDateSummary();

document.querySelector("#sample").addEventListener("click", () => {
  const sample = {date: "2018-06-15", temperature: 25, humidity: 60,
    wind_speed: 2.1, visibility: 2000, dew_point: 16.7, solar_radiation: 15,
    rainfall: 0, snowfall: 0};
  for (const [key, value] of Object.entries(sample)) form.elements.namedItem(key).value = value;
  updateDateSummary();
  errorBox.hidden = true;
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  errorBox.hidden = true;
  button.disabled = true;
  button.textContent = "예측 중…";
  resultCard.setAttribute("aria-busy", "true");
  // 새 요청이 실패했을 때 이전 결과를 새 결과처럼 표시하지 않음
  document.querySelector("#prediction").textContent = "—";
  document.querySelector("#r2").textContent = "—";
  document.querySelector("#mae").textContent = "—";
  document.querySelector("#mae-description").textContent = "일별 총 대여량의 평균 절대 오차입니다. 개별 예측의 오차 범위를 보장하지 않습니다.";
  document.querySelector("#negative-note").hidden = true;
  document.querySelector("#result-description").textContent = "입력한 조건으로 예측하고 있습니다.";
  const payload = Object.fromEntries(new FormData(form));
  for (const key of Object.keys(payload)) if (key !== "date") payload[key] = Number(payload[key]);
  const dateText = payload.date;
  try {
    if (typeof axios === "undefined") throw new Error("통신 라이브러리를 불러오지 못했습니다. 인터넷 연결을 확인하고 새로고침해 주세요.");
    const {data} = await axios.post("/bike/predict", payload, {timeout: 30000});
    if (!Number.isFinite(data.prediction) || !Number.isFinite(data.r2) || !Number.isFinite(data.mae) || data.mae < 0) throw new Error("서버의 예측 응답 형식을 확인해 주세요.");
    document.querySelector("#prediction").textContent = Math.max(0, Math.round(data.prediction)).toLocaleString("ko-KR");
    document.querySelector("#r2").textContent = data.r2.toFixed(3);
    const mae = data.mae.toLocaleString("ko-KR", {maximumFractionDigits: 1});
    document.querySelector("#mae").textContent = `${mae}대`;
    document.querySelector("#mae-description").textContent = `검증 데이터에서 실제 하루 총 대여량과 평균적으로 약 ${mae}대 차이가 났습니다. 이번 예측의 오차 범위를 보장하는 값은 아닙니다.`;
    document.querySelector("#result-description").textContent = `${dateText} · 입력한 일별 날씨 조건의 하루 총 예상 대여량입니다.`;
    document.querySelector("#negative-note").hidden = data.prediction >= 0;
  } catch (error) {
    const detail = error.response?.data?.detail;
    errorBox.textContent = typeof detail === "string" ? detail : error.response?.status === 500 ? "서버에서 예측하지 못했습니다. 모델 재학습 여부와 서버 로그를 확인해 주세요." : error.message || "예측 요청에 실패했습니다.";
    errorBox.hidden = false;
    document.querySelector("#result-description").textContent = "예측을 완료하지 못했습니다. 입력과 연결 상태를 확인해 주세요.";
  } finally {
    button.disabled = false;
    button.innerHTML = '대여량 예측하기 <span>→</span>';
    resultCard.setAttribute("aria-busy", "false");
  }
});
