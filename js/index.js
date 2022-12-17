const ROWS = 6
const COLS = 7

// generate board data

const generateBoardData = () => {
    const boardArray = []
    for(let i=0; i<COLS; i++){
        const cols = []
        for(let j=0; j<ROWS; j++){
            cols.push("0")
        }
        boardArray.push(cols)
    }
    return boardArray
}

// generate board ui

const generateBoard = () => {
    const board = document.getElementById("board")
    for(let i=1; i<=ROWS*COLS; i++){
        board.innerHTML += `
            <div id='slot${i}' class='slot'>

            </div>
        `
    }
}