// alert('create peer to peer chat please!')



// Получаем параметры запроса из URL
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

// alert(urlParams)
// Получаем конкретный параметр из URL
const intID = urlParams.get('intID');

// Выводим значение параметра в консоль
console.log(`intID = ${intID}`);


forEa

function createChatFrom (intID) {
    const chatDiv = document.getElementById('chatDiv')
    chatDiv.appendChild
    chatDiv.innerHTML = `
    <div class="messenger" id='chatDiv'>
        <!-- user title -->
        <div class="user_title">
            <div class="title">
                <button class="chat_brg" id="burger_chat"> 
                    <div></div>
                    <div></div>
                    <div></div>
                </button>
                <img class="avatar" src={% static "mainApp/img/medium.jpg" %} alt="avatar">
                <div>
                    <p>nickname</p>
                    <p class="status_info">Онлай(статус)</p>
                </div>
            </div>
            <div class="title_settings">
                <div class="search_form">
                    <button class="search_btn"></button>
                    <input placeholder="поиск"></input>
                </div>
                <div class="chat_set">
                    <button></button>
                    <ul>
                        <button>Кнопка</button>
                        <button>Кнопка</button>
                        <button>Удалить переписку</button>
                    </ul>
                    
                </div>
            </div>
        </div>



        <!-- Новые сообщения добавляются сверху (first-child) -->
        <!-- Исправить -->
        <div class="chat">
            <ul>

            </ul>
        </div>        


        <form class="input_div" method='post'>
            <span class="file_b backimgset"></span>
            <input type='hidden' name='intID' value='${intID}'></input>
            <input type='hidden' name='csrfmiddlewaretoken' value='csrf'></input>
            <textarea name='text' class="message_input" placeholder="Введите сообщение..."></textarea>
            <span class="smile backimgset"></span>
            <button class="send_b backimgset"></button>
        </form>
    </div> `
}


createChatFrom(intID)

console.log(csrf_token)