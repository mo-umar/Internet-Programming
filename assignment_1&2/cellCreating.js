// Dynamic cell create and sort
let count = 1;

function addCell() {
  let table = document.getElementById('cell_field');
  let row = document.getElementById("cell_row" +  count.toString())

  if (row != null) {
    row.style.display = "table-row";
    count++;
  }
  else {
    let new_row = table.insertRow(-1);
    new_row.id = "cell_row" + count.toString();
    let index = new_row.insertCell(0);
    let entry_cell = new_row.insertCell(1);
    let length_cell = new_row.insertCell(2);
    index.innerText = count.toString();
    entry_cell.innerHTML = "<input type='text' id=" + "entry_field" + count.toString() + "></input>";
    document.getElementById("entry_field" + count.toString()).oninput = calcLength;
    length_cell.innerHTML = "0";
    length_cell.id = "entry_field" + count.toString() + "length"
    length_cell.style.textAlign = "center";
    count++;
  }

}

function removeCell() {
  let name = "cell_row" + (count - 1).toString();
  let row = document.getElementById(name);

  if (row == null) {
    return;
  }

  else {
    row.style.display = "none";
    if (count > 0) {
      count--;
    }
  }
}

function sortCells() {
  let cells = [];

  for (let i = 1; i < count; i++) {
    let entry_field = document.getElementById("entry_field" + i.toString());
    cells.push(entry_field.value)
  }

  cells.sort()
  cells = removeBlanks(cells);

  for (let j = 1; j < count; j++) {
    let entry_field = document.getElementById("entry_field" + j.toString());

    if (cells[(j-1)] !== undefined) {
      entry_field.value = cells[(j-1)].toString();
      document.getElementById("entry_field" + j.toString() + "length").innerText = entry_field.value.length.toString();
    }

    else {
      entry_field.value = "";
      document.getElementById("entry_field" + j.toString() + "length").innerText = entry_field.value.length.toString();
    }
  }
}

function calcLength() {
  let contents = this.value.length;
  let id = this.id + "length"
  document.getElementById(id).innerText = contents
}

function removeBlanks(oldArray) {
  let newArray = [];
  let numBlanks = 0;

  for (let i = 0; i < oldArray.length; i++) {
    if (oldArray[i] !== "") {
      newArray.push(oldArray[i]);
      numBlanks++;
    }
  }

  for (blank in numBlanks) {
    newArray.push("");
  }

  return newArray;
}