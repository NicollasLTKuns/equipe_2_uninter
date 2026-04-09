let jogador = document.getElementById("vez")
let btn = document.querySelectorAll(" .Tab")

let vez = "X"
let start = true
const vitorias = [
  [0,1,2], [3,4,5], [6,7,8],
  [0,3,6], [1,4,7], [2,5,8],
  [0,4,8], [2,4,6]
];


btn.forEach((btn, i) => {
    
    btn.onclick = () => {
        if (btn.innerText || !start)return
        
        btn.innerText = vez
        
        if (ganhou()){
          start = false
          setTimeout(() => {
            alert("O jogador " + vez + " ganhou!!!")
            location.reload()
          }, 250)
        }
        vez = vez === "X" ? "O" : "X"
        jogador.innerText = `Vez do jogador: ${vez}`
    }  
})
function ganhou() {
  return vitorias.some(c =>
    btn[c[0]].innerText &&
    btn[c[0]].innerText === btn[c[1]].innerText &&
    btn[c[0]].innerText === btn[c[2]].innerText
  );
}