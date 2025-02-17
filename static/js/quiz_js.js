let resetTimer = false;

function hideAllQuestions(elStorage) {
    for (let i = 1; i < 6; i++) {
        let questionEl = document.getElementById(`question-number${i}`);
        elStorage.push(questionEl);
        questionEl.remove();
    }
    return elStorage;
}

function takeQuestion(elStorage) {
    let question = elStorage.shift();
    let jsContainer = document.getElementById('js_container');
    jsContainer.appendChild(question);

    return elStorage;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function makeGreen() {
    let correctAnswer = document.getElementById("valid-option");
    let text = correctAnswer.textContent;
    let button = document.getElementById(`${text}`);
    button.style.backgroundColor = "lightgreen";

}

function manageButtons(num) {
    let buttons = document.getElementsByClassName(`options${num}`);
    for (let button of buttons) {
        button.addEventListener("click", hideQuestion);

        async function hideQuestion() {
            let section = button.parentElement;
            let question = section.parentElement;
            makeGreen();
            await sleep(1000);
            resetTimer = true;
            question.remove();
            return resetTimer;
        }
    }


    return resetTimer;
}



async function mainLoop() {
    let elStorage = [];
    let counterAnsweredCorrect = 0;
    elStorage = hideAllQuestions(elStorage);
    let h1 = document.getElementById("timer");
    for (let i = 1; i <= 5; i++) {
        elStorage = takeQuestion(elStorage)
        let time = 15;
        resetTimer = manageButtons(i);
        while (time > 0) {
            await sleep(1000);
            h1.textContent = time;
            if (resetTimer) {
                h1.textContent = '';
                break;
            }
            time -= 1;
            if (time === 0) {
                let question = document.getElementById(`question-number${i}`);
                question.remove();
            }
        }
        if (resetTimer) {
            resetTimer = false;
        }
    }
    h1.remove();

}


