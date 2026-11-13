const dateInput=document.querySelector('#atvetel');
if(dateInput){
  const tomorrow=new Date();tomorrow.setDate(tomorrow.getDate()+1);
  dateInput.min=`${tomorrow.getFullYear()}-${String(tomorrow.getMonth()+1).padStart(2,'0')}-${String(tomorrow.getDate()).padStart(2,'0')}`;
  const requested=new URLSearchParams(location.search).get('termek');
  if(requested==='torta')document.querySelector('#termek').value='torta';
  const form=dateInput.form;
  form.addEventListener('submit',event=>{
    const error=form.querySelector('.form-error');error.hidden=true;
    const day=new Date(`${dateInput.value}T12:00:00`).getDay();
    if(day===0||day===1){event.preventDefault();error.textContent='Átvételre kedd és szombat között válassz napot.';error.hidden=false;dateInput.focus();return}
    if(location.protocol==='file:'){event.preventDefault();error.textContent='A próbaoldalon az űrlap még nem küld üzenetet. Az élesítés után működik majd.';error.hidden=false;return}
  });
}
const contactForm=document.querySelector('form[name="erdeklodes"]');
if(contactForm&&location.protocol==='file:')contactForm.addEventListener('submit',event=>{event.preventDefault();const error=contactForm.querySelector('.form-error');error.textContent='A próbaoldalon az űrlap még nem küld üzenetet. Az élesítés után működik majd.';error.hidden=false});
