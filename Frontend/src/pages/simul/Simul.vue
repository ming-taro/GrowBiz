<template>
  <div v-if="isLoading == false">
    <div class="animation-container">
      <div class="progress-container">
        <div class="progress-bar" :style="{ width: progressBarWidth }"></div>
      </div>
      <img src="@/assets/img/simul/sumul_cut.jpg" alt="Background Image" class="background-image" />
      <img src="@/assets/img/simul/leaf1.png" alt="Leaf" class="leaf-animation1" />
      <img src="@/assets/img/simul/leaf2.png" alt="Leaf" class="leaf-animation2" />
      <img src="@/assets/img/simul/leaf3.png" alt="Leaf" class="leaf-animation3" />
      <img src="@/assets/img/simul/leaf4.png" alt="Leaf" class="leaf-animation4" />
      <img src="@/assets/img/simul/leaf1.png" alt="Leaf" class="leaf-animation5" />

      <div v-if="showSpeechBubble">
        <img src="@/assets/img/simul/speech_bubble_no.png" alt="Speech Bubble" class="speech-bubble" />
        <div class="answer-box">
          <div v-if="showChoices" class="choices_2">
            <div v-for="(choice, index) in choices" :key="index">
              <button @mouseover="isHovered = choice.text" @mouseleave="isHovered = ''"
                @click="updateChoice(choice.text, index)">
                <span class="arrow">{{
                  isHovered === choice.text ? '▶' : ''
                }}</span>
                <span class="text">{{ choice.text }}</span>
              </button>
            </div>
          </div>
          <div v-if="questionID == 0" class="button-container">
            <button class="retry-button" @click="retry()">다시 선택하기</button>
          </div>
        </div>
      </div>
      <img v-else src="@/assets/img/simul/speech_bubble_no.png" alt="Speech Bubble No" class="speech-bubble" />

      <div class="main_text_animation">
        <p class="text-line" v-html="typedTextLine1"></p>
        <p class="text-line" v-html="typedTextLine2" v-show="typedTextLine2.length > 0"></p>
      </div>
    </div>
  </div>

  <div v-else>
    <div class="animation-container">
      <img src="@/assets/img/simul/report_loading.jpg" alt="Background Image" class="background-image" />
      <div class="loading-text">시뮬레이션 결과를 준비 중입니다...</div>
      <div class="loader"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { getQuestions, createSimulationAnswer, executeFranchiseAnalyze } from '@/services/simulation/SimulationAPI';
import { useAuthStore } from '@/stores/auth';
import { findReportIdByResponseId } from '@/services/simulation/ReportAPI';

const authStore = useAuthStore();

const questions = ref([]);
const questionID = ref(-1);
const choices = ref([]);
let lastQuestionID = 0;

const currentChoices = ref([]);
const currentChoiceType = ref(0);
const choiceType = ref({}); // 질문 유형
let userChoice = {}; // 유저가 선택한 답변

const userAnswers = {};

const typedTextLine1 = ref('');
const typedTextLine2 = ref('');
const showSpeechBubble = ref(false);
const showChoices = ref(false);
const isHovered = ref('');

const totalSteps = ref(10); // 총 단계

const isLoading = ref(false);

// 진행도 비율 계산
const progressBarWidth = computed(() => {
  return `${((questionID.value + 1) / totalSteps.value) * 100}%`;
});

const typeQuestion = (fullText) => {
  const result = fullText.split(" ");
  let text = "";
  let nextText = "";

  for (let i = 0; i < result.length; i++) {
    if (text.length + result.length <= 24) {
      text += result[i] + " ";
    } else {
      nextText += result[i] + " ";
    }
  }

  typedTextLine1.value = ""; // 질문지 갱신
  typedTextLine2.value = "";

  typeText(text, typedTextLine1, nextText);
}

const typeText = (text, typedText, nextText, delay = 0) => {
  showSpeechBubble.value = false;
  showChoices.value = false;
  const letters = text.split('');
  let index = 0;

  const interval = setInterval(() => {
    if (index < letters.length) {
      typedText.value += letters[index];
      index++;
    } else {
      clearInterval(interval);
      if (nextText) {
        setTimeout(() => {
          typeText(
            nextText,
            typedText === typedTextLine1 ? typedTextLine2 : null
          );
        }, 500);
      } else {
        setTimeout(() => {
          showSpeechBubble.value = true;
          showChoices.value = true;
        }, 500);
      }
    }
  }, 40);
};

const findChoiceType = (choice) => {
  if ("district" in choice) {
    return { 0: "district", 1: "neighborhoods" };
  } else if ("category" in choice) {
    return { 0: "category", 1: "subcategories" };
  }
  return { 0: "text" }
}

const isLastChoice = () => {
  if ((currentChoiceType.value + 1) in choiceType.value) {
    return false;
  }
  return true;
}

const isLastQuestion = () => {
  return questions.value[questionID.value].ind == lastQuestionID;
}

const moveReportPage = async () => {
  try {
    const simulationResponse = await createSimulationAnswer(authStore.id, userAnswers);
    console.log("만들어진 응답:", simulationResponse);
    // const report = await createReport(authStore.id, simulationResponse.id);
    // console.log("만들어진 리포트:", report);

    isLoading.value = true;
    let startTime = performance.now();

    // let response = await executeFranchiseAnalyze(report.id);

    let reportId = await executeFranchiseAnalyze(simulationResponse.id);
    let endTime = performance.now();

    // 시간 차이 계산 (밀리초 단위)
    let timeTaken = endTime - startTime;
    isLoading.value = false;

    // const reportId = await findReportIdByResponseId(simulationResponse.id);

    // console.log("소요 시간", timeTaken / 1000, "초");
    location.href = `/simul/report?id=${reportId}`; // 리포트 페이지로 이동
    // console.log("응답 아이디:", simulationResponse.id);
    // console.log("리포트 아이디:", reportId);
  } catch (error) {
    console.error("Error during saving simulation answer:", error);
  }
};

const updateFirstChoice = () => {
  userChoice = {};             // 유저 답변 초기화
  currentChoiceType.value = 0; // 선택 번호 초기화
  currentChoices.value = questions.value[questionID.value].choices;
  choiceType.value = findChoiceType(questions.value[questionID.value].choices[0]); // 질문에 대한 답변 유형 갱신

  typeQuestion(questions.value[questionID.value].fullTexts)

  let dataType = choiceType.value[currentChoiceType.value];

  choices.value = [];
  for (let i = 0; i < currentChoices.value.length; i++) {
    choices.value.push({ text: currentChoices.value[i][dataType], value: currentChoices.value[i].value });
  }
}

const updateChoice = async (choice, index) => {
  let dataType = choiceType.value[currentChoiceType.value];
  if (dataType == 'text') {
    userChoice[dataType] = choices.value[index].value;
  } else {
    userChoice[dataType] = choice;
  }

  if (isLastChoice()) {
    userAnswers[questionID.value] = userChoice;

    if (isLastQuestion()) {
      moveReportPage();
      return;
    }

    questionID.value += 1;
    updateFirstChoice();
    return;
  }

  currentChoices.value = currentChoices.value[index];
  currentChoiceType.value += 1; // 같은 질문의 다음 선택으로 넘어감

  choices.value = [];
  dataType = choiceType.value[currentChoiceType.value];

  for (let i = 0; i < currentChoices.value[dataType].length; i++) {
    if (questionID.value == 0) { // 위치 선택 질문
      choices.value.push({
        text: currentChoices.value[dataType][i],
        value: i
      });
    } else { // 업종 선택 질문
      choices.value.push({
        text: currentChoices.value[dataType][i].text,
        value: i
      });
    }
  }
}

const fetchQuestions = async () => {
  try {
    questions.value = await getQuestions();
    if (questions.value.length > 0) {
      totalSteps.value = questions.value.length;
      questionID.value += 1;       // 첫 번째 질문
      updateFirstChoice();

      lastQuestionID = questions.value[questions.value.length - 1].ind;
    }
  } catch (error) {
    console.error('Failed to fetch questions:', error);
  }
};

const retry = () => {
  currentChoiceType.value = 0;
  updateFirstChoice();
}

onMounted(async () => {
  await fetchQuestions(); // 질문 가져오기
});
</script>

<style scoped>
.loading-text {
  position: absolute;
  top: 30%;
  left: 48%;
  transform: translate(-50%, -50%);
  z-index: 9999;
  font-size: 24px;
  font-weight: bold;
  color: #fff;
  background-color: rgba(0, 0, 0, 0.6);
  padding: 10px 20px;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.loader {
  position: absolute;
  top: 50%;
  left: 45%;
  transform: translate(-50%, -50%);
  border: 16px solid #f3f3f3;
  border-top: 16px solid #3498db;
  border-radius: 50%;
  width: 100px;
  height: 100px;
  animation: spin 2s linear infinite;
  z-index: 9999;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

/* 타자 애니메이션 스타일 */
.main_text_animation {
  position: absolute;
  bottom: 85px;
  /* Adjust position as needed */
  left: 31%;
  /* 왼쪽에서 시작하도록 변경 */
  color: #000;
  /* 텍스트 색상 */
  text-align: left;
  /* 왼쪽 정렬 */
}

.text-line {
  font-size: 35px;
  /* 텍스트 크기 */
  font-weight: bold;
  margin: 0;
  /* 기본 마진 제거 */
  position: absolute;
  /* 절대 위치 지정 */
  white-space: nowrap;
  /* 텍스트가 줄바꿈되지 않도록 설정 */
}

.text-line:nth-child(1) {
  bottom: 60px;
  /* 첫 번째 줄의 위치 */
}

.text-line:nth-child(2) {
  bottom: 0px;
  /* 두 번째 줄의 위치 (필요에 따라 조정) */
}

.animation-container {
  position: relative;
  width: 100%;
  height: 712px;
}

.background-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.speech-bubble {
  position: absolute;
  bottom: 5px;
  /* Adjust the distance from the bottom */
  left: 50%;
  /* Center horizontally */
  transform: translateX(-48%);
  /* Centering adjustment */
  width: 77%;
  /* Set the width to 70% */
  opacity: 1;
  transition: opacity 0.5s ease;
  /* 자연스러운 등장 효과 */
}

.leaf-animation1,
.leaf-animation2,
.leaf-animation3,
.leaf-animation4,
.leaf-animation5 {
  position: absolute;
  top: -100px;
  width: 50px;
  /* Adjust the size of the leaf */
  animation: leaf-fall linear infinite;
}

/* Add different initial positions, animation durations, and delays */
.leaf-animation1 {
  left: 10%;
  animation-duration: 8s;
  animation-delay: 0s;
}

.leaf-animation2 {
  left: 25%;
  animation-duration: 17s;
  animation-delay: 0.5s;
}

.leaf-animation3 {
  left: 80%;
  animation-duration: 10s;
  animation-delay: 2s;
}

.leaf-animation4 {
  left: 70%;
  animation-duration: 8s;
  animation-delay: 1s;
}

.leaf-animation5 {
  left: 90%;
  animation-duration: 17s;
  animation-delay: 0.5s;
}

@keyframes leaf-fall {
  0% {
    transform: translate(-50%, 0) rotate(0deg);
    opacity: 1;
  }

  100% {
    transform: translate(-50%, 800px) rotate(360deg);
    opacity: 1;
  }
}

/* 선택지 스타일 */
.header-info-choices_2 {
  display: block;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: white;
  border-radius: 20px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-height: 0;
  overflow: hidden;
  opacity: 0;
  transition: max-height 0.3s ease, opacity 0.3s ease;
}

.choices_2 {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  height: auto;
  max-height: 300px;
  overflow-y: auto;
  margin: 30px 15px 30px 25px;
  padding: 0px 0px 10px 0px;
}

/* 스크롤바 스타일링 */
.choices_2::-webkit-scrollbar {
  width: 10px;
  /* 스크롤바 너비 */
}

.choices_2::-webkit-scrollbar-track {
  background: #f0f0f0;
  /* 스크롤바 배경 색상 */
  border-radius: 10px;
  /* 모서리 둥글게 */
}

.choices_2::-webkit-scrollbar-thumb {
  background: #c0c0c0;
  /* 스크롤바 색상 */
  border-radius: 10px;
  /* 모서리 둥글게 */
}

.choices_2::-webkit-scrollbar-thumb:hover {
  background: #a0a0a0;
  /* 호버 시 색상 */
}

/* 스크롤박스가 호버할 때 스크롤바 보이기 */
.choices_2:hover::-webkit-scrollbar {
  opacity: 1;
  /* 스크롤바가 보이도록 설정 */
}

.button-container {
  display: flex;
  /* Flexbox 활성화 */
  justify-content: center;
  /* 가운데 정렬 */
  width: 100%;
  /* 전체 너비 차지 */
  margin-bottom: 10px;
  /* 버튼 간격 조정 */
}

.retry-button {
  background-color: #f39c12;
  /* 어울리는 배경색으로 수정 */
  color: white;
  /* 글자 색상 */
  border: none;
  /* 테두리 없음 */
  border-radius: 25px;
  /* 모서리 둥글게 */
  padding: 10px 15px;
  /* 패딩 */
  cursor: pointer;
  /* 커서 포인터로 변경 */
  transition: background-color 0.3s;
  /* 배경색 변화 효과 */
}

.retry-button:hover {
  background-color: #e67e22;
  /* 호버 시 배경색 */
}

.retry-button:active {
  background-color: #d35400;
  /* 클릭 시 배경색 */
}

.choices_2 div {
  margin-bottom: -5px;
  /* 버튼 간 간격을 줄이기 */
}

.choices_2 button {
  padding: 10px 15px;
  /* 수직 패딩과 수평 패딩 설정 */
  cursor: pointer;
  display: flex;
  /* 플렉스 박스를 사용하여 정렬 */
  align-items: center;
  /* 세로 중앙 정렬 */
  font-size: 20px;
  /* 폰트 크기 */
  background-color: transparent;
  /* 기본 배경 색상 */
  border-radius: 25px;
  /* 둥근 모서리 */
  color: black;
  /* 텍스트 색상 */
  border: none;
  /* 테두리 없음 */
  text-align: left;
  /* 텍스트 왼쪽 정렬 */
  transition: background-color 0.3s ease;
  /* 배경 색상 전환 효과 */
}

.choices_2 button span.arrow {
  width: 20px;
  /* 화살표 크기 고정 */
  font-size: 14px;
}

.choices_2 button:hover {
  background-color: #fcd752;
  /* 호버 시 배경 색상 */
  border-radius: 25px;
  font-weight: bold;
  padding: 10px 20px;
  /* 여백을 다시 설정하여 안정성 확보 */
}

/* 선택지 텍스트가 밀리지 않도록 고정 */
.choices_2 button span.text {
  padding-left: 5px;
  /* 화살표를 위한 여백 추가 */
}

.answer-box {
  background-color: #fee9b4;
  position: absolute;
  bottom: 185px;
  /* Adjust position as needed */
  left: 74%;
  /* Center horizontally */
  transform: translateX(-50%);
  /* Centering adjustment */
  width: 230px;
  border-radius: 80px;
  /* width: auto;
  white-space: nowrap; */
}

.progress-container {
  position: absolute;
  top: 9%;
  bottom: 150px;
  /* Adjust as needed */
  left: 50%;
  transform: translateX(-50%);
  width: 58%;
  /* 바의 전체 너비 */
  height: 20px;
  /* 바의 높이 */
  background-color: #e0e0e0;
  /* 배경 색상 */
  border-radius: 10px;
  /* 둥근 모서리 */
  overflow: hidden;
  /* 내부 바가 넘치지 않도록 설정 */
}

.progress-bar {
  height: 100%;
  background-color: #76c7c0;
  /* 진행도 색상 */
  border-radius: 10px;
  /* 둥근 모서리 */
  transition: width 0.3s ease;
  /* 자연스러운 전환 효과 */
}
</style>