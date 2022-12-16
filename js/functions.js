// FUNCTIONS

// print board
export const printBoard = (cols) => {
    for(let i=0;i<ROWS;i++){
        console.log(" ")
        for(let j=0;j<COLS;j++){
            process.stdout.write(cols[j][i].toString())
        }
    }
}