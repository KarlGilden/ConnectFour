// constants
const ROWS = 6
const COLS = 7

// game variables
var boardData;
var player;

// generate init board data

const generateBoardData = () => {
    var boardArray = []
    for(let i=0; i<COLS; i++){
        const cols = []
        for(let j=0; j<ROWS; j++){
            cols.push("b")
        }
        boardArray.push(cols)
    }
    return boardArray
}

// generate board ui

const generateBoard = () => {
    const boardElement = document.getElementById("board")

    boardElement.innerHTML = ``

    for(let i=0; i<boardData.length; i++){
        const reversedBoard = boardData[i].slice().reverse()
        boardElement.innerHTML += `
            <div onclick={takeTurn(${i})} id='col${i}' class='col'>
                ${reversedBoard.map((value, index)=>{
                    return `<div id='slot${index}' class='slot ${value}'>

                        </div>`
                })}
            </div>
        `
    }
}

// user turn

const takeTurn = (col) => {
    const turnIndicator = document.getElementById("turn-indicator");
    const token = player ? "r" : "y"

    // update data
    const row = updateData(token, col)

    // update ui
    generateBoard()

    // check for win
    const y = checkY(token, col, row)
    const x = checkX(token, col, row)
    const rd = checkRD(token, col, row)
    const ld = checkLD(token, col, row)

    if(y || x || rd || ld){ 
        document.getElementById("body").innerHTML += `
            <div id="win-screen" class="win-screen">
                <div class="win-wrapper">
                    <h1 class="win-title">Winner!</h1>
                    <div class='win-token ${token}'></div>
                    <button class='play-button' onclick="playAgain()">Play again</button>
                </div>
            </div>
        `
        
    }

    if(row != null) player = !player

    turnIndicator.textContent = player ? "🔴's turn" : "🟡's turn";
}

// update board
const updateData = (token, col) => {
    var row = boardData[col].indexOf("b")
    if(row == -1){
        return null
    }
    boardData[col][row] = token
    return row
    
}

// check winning states
const checkY = (token, col, row) => {
    var connected = 0
    var up = row
    var down = row

    while(up < ROWS && up >= 0){
        if(boardData[col][up] != token) break

        connected += 1

        if(connected >= 5) return true

        up++
    }

    while(down < ROWS && down >= 0){
        if(boardData[col][down] != token) break

        connected += 1

        if(connected >= 5) return true

        down--
    }

    return false
}

const checkX = (token, col, row) => {
    var connected = 0
    var left = col
    var right = col

    while(right < COLS && right >= 0){
        if(boardData[right][row] != token) break

        connected += 1

        if(connected >= 5) return true

        right++
    }

    while(left < COLS && left >= 0){
        if(boardData[left][row] != token) break

        connected += 1

        if(connected >= 5) return true

        left--
    }

    return false
}

const checkRD = (token, col, row) => {
    var connected = 0
    var left = col
    var right = col
    var up = row
    var down = row

    while(right < COLS && right >= 0 && up < ROWS && up >= 0){
        if(boardData[right][up] != token) break

        connected += 1

        if(connected >= 5) return true

        right++
        up++
    }

    while(left < COLS && left >= 0 && down < ROWS && down >= 0){
        if(boardData[left][down] != token) break

        connected += 1

        if(connected >= 5) return true

        left--
        down--
    }

    return false
}

const checkLD = (token, col, row) => {
    var connected = 0
    var left = col
    var right = col
    var up = row
    var down = row

    while(right < COLS && right >= 0 && down < ROWS && down >= 0){
        if(boardData[right][down] != token) break

        connected += 1

        if(connected >= 5) return true

        right++
        down--
    }

    while(left < COLS && left >= 0 && up < ROWS && up >= 0){
        if(boardData[left][up] != token) break

        connected += 1

        if(connected >= 5) return true

        left--
        up++
    }

    return false
}

const playAgain = () => {
    initialiseGame();
    document.getElementById("win-screen").remove()
}

const initialiseGame = () => {
    const turnIndicator = document.getElementById("turn-indicator");
    turnIndicator.textContent = "🟡 starts"

    // set player
    player = false

    // generate board data
    boardData = generateBoardData()

    // generate board UI
    generateBoard()
}

initialiseGame();


