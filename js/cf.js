const readline = require('readline');

// FUNCTIONS

const printBoard = (c) => {
    for(let i=0;i<ROWS;i++){
        console.log(" ")
        for(let j=0;j<COLS;j++){
            process.stdout.write(c[j][i].toString())
        }
    }
}

const promptUser = () => {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
      });

    return new Promise(resolve => rl.question('Pick a column:', col => {
        rl.close();
        resolve(col)
    }));
}

// GAME

console.log("||| Connect Four |||")

const ROWS = 6
const COLS = 7

// init board
var cols = [[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

var playing = true

// print board
printBoard(cols)

while(playing){
    // prompt user
    (async ()=>{
        const col = await promptUser()
        cols[col].push(1)
        cols[col].shift()
    })()
}

  



