/**
 * Get a jQuery object for a specific cell.
 */
function getCellElem(row, col) {
    return $("#board-cell-" + row + "-" + col);
}

/**
 * Get a string representing the state of the game board at row, col.
 *
 * See getCellStrForElem() for info about the return type.
 */
function getCellStr(row, col) {
    var cellElem = getCellElem(row, col);
    return getCellStrForElem(cellElem.get())
}

/**
 * Get a string for the cell represented by the given DOM element.
 *
 * Returns ' ' for an empty cell, 'X' for a cell taken by X, and 'O' for a
 * cell taken by O.
 */
function getCellStrForElem(elem) {
    var content = $(elem).text();

    // empty cells are represented with a space char
    if(!content.trim()) {
        content = ' ';
    }

    return content;
}


/**
 * Get a list of strings representing the current board.
 */
function getBoard() {
    var board = []
    for(var row = 0; row < 3; row++) {
        var rowStr = ''
        for(var col = 0; col < 3; col++) {
            var content = getCellStr(row, col);
            rowStr += content;
        }
        board.push(rowStr);
    }
    return board;
}


/**
 * Mark the cell at row, col for the player.
 *
 * Returns true if it succeeded, and false if it failed (i.e. the cell
 * has already been taken).
 */
function takeCell(cellElem) {
    var cell = getCellStrForElem(cellElem);
    if(cell != ' ') {
        return false;
    } else {
        $(cellElem).text('X');
        return true;
    }
}


$(document).ready(function() {
    $("#tictactoe-board td").click(function() {
        takeCell(this);
    });
});