//apresenta o formulário de acordo com o que for selecionado
document.addEventListener('DOMContentLoaded', function() {
    const ramo = document.getElementById('ramo_empresa');
    const producao = document.getElementById('producao');
    const agro = document.getElementById('agro')

//apresenta o formulário conforme o ramo selecionado
    ramo.addEventListener('change', function() {

        agro.classList.remove('mostrar');
        producao.classList.remove('mostrar');

        agro.style.display = 'none';
        producao.style.display = 'none';

        if (this.value === '1') {
            agro.style.display = 'block';
            agro.classList.add('mostrar');
        } else if (this.value === '2') {
            producao.style.display = 'block';
            producao.classList.add('mostrar');
        } else {
            producao.style.display = 'none';
            agro.style.display = 'none';
        }
    });
})

//Função oculta campo gasolina, aparece quando selecionado
function toggleGasolina() {
    const checkGasolina = document.getElementById('checkGasolina');
    const gasolina = document.getElementById('gasolina');
    const txGasolina = document.getElementById('txGasolina');
    const tx_qtGasolina = document.getElementById('tx_qtGasolina');
    const qtGasolina = document.getElementById('qtGasolina');

    gasolina.classList.remove('mostrar');
    txGasolina.classList.remove('mostrar');
    tx_qtGasolina.classList.remove('mostrar');
    qtGasolina.classList.remove('mostrar');

    if (checkGasolina.checked) {
        gasolina.style.display = 'block';
        txGasolina.style.display = 'block';
        tx_qtGasolina.style.display = 'block';
        qtGasolina.style.display = 'block';
    } else {
        gasolina.style.display = 'none';
        txGasolina.style.display = 'none';
        tx_qtGasolina.style.display = 'none';
        qtGasolina.style.display = 'none';
    }
}
//Função oculta campo etanol, aparece quando selecionado
function toggleEtanol() {
    const checkEtanol = document.getElementById('checkEtanol');
    const etanol = document.getElementById('etanol');
    const txEtanol = document.getElementById('txEtanol')
    const tx_qtEtanol = document.getElementById('tx_qtEtanol')
    const qtEtanol = document.getElementById('qtEtanol')

    etanol.classList.remove('mostrar');
    txEtanol.classList.remove('mostrar');
    tx_qtEtanol.classList.remove('mostrar')
    qtEtanol.classList.remove('mostrar')

    if (checkEtanol.checked) {
        etanol.style.display = 'block';
        txEtanol.style.display = 'block';
        tx_qtEtanol.style.display = 'block';
        qtEtanol.style.display = 'block';
    } else {
        etanol.style.display = 'none';
        txEtanol.style.display = 'none';
        tx_qtEtanol.style.display = 'none';
        qtEtanol.style.display = 'none';
    }
}
//Função oculta campo diesel, aparece quando selecionado
function toggleDiesel() {
    const checkDiesel = document.getElementById('checkDiesel');
    const diesel = document.getElementById('diesel');
    const txDiesel = document.getElementById('txDiesel')
    const tx_qtDiesel = document.getElementById('tx_qtDiesel');
    const qtDiesel = document.getElementById('qtDiesel');

    diesel.classList.remove('mostrar');
    txDiesel.classList.remove('mostrar');
    tx_qtDiesel.classList.remove('mostrar')
    qtDiesel.classList.remove('mostrar');

    if (checkDiesel.checked) {
        diesel.style.display = 'block';
        txDiesel.style.display = 'block';
        tx_qtDiesel.style.display = 'block';
        qtDiesel.style.display = 'block'
    } else {
        diesel.style.display = 'none';
        txDiesel.style.display = 'none';
        tx_qtDiesel.style.display = 'none';
        qtDiesel.style.display = 'none';
    }
}
//Função oculta campo biodiesel, aparece quando selecionado
function toggleBiodiesel() {
    const checkBiodiesel = document.getElementById('checkBiodiesel');
    const biodiesel = document.getElementById('biodiesel');
    const txBiodiesel = document.getElementById('txBiodiesel');
    const tx_qtBiodiesel = document.getElementById('tx_qtBiodiesel');
    const qtBiodiesel = document.getElementById('qtBiodiesel');

    biodiesel.classList.remove('mostrar');
    txBiodiesel.classList.remove('mostrar');
    tx_qtBiodiesel.classList.remove('mostrar');
    qtBiodiesel.classList.remove('mostrar');

    if (checkBiodiesel.checked) {
        biodiesel.style.display = 'block';
        txBiodiesel.style.display = 'block';
        tx_qtBiodiesel.style.display = 'block';
        qtBiodiesel.style.display = 'block';
    } else {
        biodiesel.style.display = 'none';
        txBiodiesel.style.display = 'none';
        tx_qtBiodiesel.style.display = 'none';
        qtBiodiesel.style.display = 'none';
    }
}
document.addEventListener('DOMContentLoaded', function() {
    toggleGasolina();
    toggleEtanol();
    toggleDiesel();
    toggleBiodiesel();
});

//função oculta campo produção de aço
function toggleAco() {
    const checkAco = document.getElementById('checkAco');
    const txProdAco = document.getElementById('txProdAco');
    const ProdAco = document.getElementById('ProdAco');

    if (checkAco.checked) {
        txProdAco.style.display = 'block';
        ProdAco.style.display = 'block';
    } else {
        txProdAco.style.display = 'none';
        ProdAco.style.display = 'none';

    }
}

//função oculta campo produção de Cimento
function toggleCimento(){
    const checkCimento = document.getElementById('checkCimento');
    const txProdCimento = document.getElementById('txProdCimento');
    const ProdCimento = document.getElementById('ProdCimento');

    if (checkCimento.checked) {
        txProdCimento.style.display = 'block';
        ProdCimento.style.display = 'block';
    }else{
        txProdCimento.style.display = 'none';
        ProdCimento.style.display = 'none';
    }

}

//função oculta campo produção de papel
function togglePapel(){
    const checkPapel = document.getElementById('checkPapel');
    const txProdPapel = document.getElementById('txProdPapel');
    const ProdPapel = document.getElementById('ProdPapel');

    if (checkPapel.checked){
        txProdPapel.style.display = 'block';
        ProdPapel.style.display = 'block';
    } else {
        txProdPapel.style.display = 'none';
        ProdPapel.style.display = 'none';
    }
}

//função oculta campo produção de vidro
function toggleVidro(){
    const checkVidro = document.getElementById('checkVidro');
    const txProdVidro = document.getElementById('txProdVidro');
    const ProdVidro = document.getElementById('ProdVidro');

    if (checkVidro.checked){
        txProdVidro.style.display = 'block';
        ProdVidro.style.display = 'block';
    } else {
        txProdVidro.style.display = 'none';
        ProdVidro.style.display = 'none';
    }

}

//função oculta campo produção de alumínio
function toggleAluminio(){
    const checkAluminio = document.getElementById('checkAluminio');
    const txProdAluminio = document.getElementById('txProdAluminio');
    const ProdAluminio =document.getElementById('ProdAluminio');

    if (checkAluminio.checked) {
        txProdAluminio.style.display = 'block';
        ProdAluminio.style.display = 'block';
    } else{
        txProdAluminio.style.display = 'none';
        ProdAluminio.style.display = 'none';
    }
}

//função oculta campo produção de etanol
function toggleProdEtanol(){
    const checkProdEtanol = document.getElementById('checkProdEtanol');
    const txProdEtanol = document.getElementById('txProdEtanol');
    const ProdEtanol = document.getElementById('ProdEtanol');

    if (checkProdEtanol.checked) {
        txProdEtanol.style.display = 'block';
        ProdEtanol.style.display = 'block';
    } else{
        txProdEtanol.style.display = 'none';
        ProdEtanol.style.display = 'none';
    }
}

//função oculta campo produção de Amonia
function toggleAmonia(){
    const checkAmonia = document.getElementById('checkAmonia');
    const txProdAmonia = document.getElementById('txProdAmonia');
    const ProdAmonia =document.getElementById('ProdAmonia');

    if (checkAmonia.checked) {
        txProdAmonia.style.display = 'block';
        ProdAmonia.style.display = 'block';
    } else{
        txProdAmonia.style.display = 'none';
        ProdAmonia.style.display = 'none';
    }
}

//função oculta campo produção de eletricidade por carvão
function toggleEleCarvao(){
    const checkEleCarvao = document.getElementById('checkEleCarvao');
    const txEleCarvao = document.getElementById('txEleCarvao');
    const ProdEletricidade_Carvao =document.getElementById('ProdEletricidade_Carvao');

    if (checkEleCarvao.checked) {
        txEleCarvao.style.display = 'block';
        ProdEletricidade_Carvao.style.display = 'block';
    } else{
        txEleCarvao.style.display = 'none';
        ProdEletricidade_Carvao.style.display = 'none';
    }
}

//função oculta campo produção de eletricidade por Gás Natural
function toggleEleGas(){
    const checkEleGas = document.getElementById('checkEleGas');
    const txEleGas = document.getElementById('txEleGas');
    const ProdEletricidade_GasNat =document.getElementById('ProdEletricidade_GasNat');

    if (checkEleGas.checked) {
        txEleGas.style.display = 'block';
        ProdEletricidade_GasNat.style.display = 'block';
    } else{
        txEleGas.style.display = 'none';
        ProdEletricidade_GasNat.style.display = 'none';
    }
}

//função oculta campo produção de eletricidade por carvão
function toggleElePetroleo(){
    const checkElePetroleo = document.getElementById('checkElePetroleo');
    const txElePetroleo = document.getElementById('txElePetroleo');
    const ProdEletricidade_Petroleo =document.getElementById('ProdEletricidade_Petroleo');

    if (checkElePetroleo.checked) {
        txElePetroleo.style.display = 'block';
        ProdEletricidade_Petroleo.style.display = 'block';
    } else{
        txElePetroleo.style.display = 'none';
        ProdEletricidade_Petroleo.style.display = 'none';
    }
}
document.addEventListener('DOMContentLoaded',function (){
    toggleAco(); //chama função para ocultar o campo aço
    toggleCimento(); //chama função para ocultar o campo cimento
    togglePapel(); //chama função para ocultar o campo pepel
    toggleVidro(); //chama função para ocultar o campo vidro
    toggleAluminio(); //chama função para ocultar o campo alumínio
    toggleProdEtanol(); //chama função para ocultar o campo Etanol
    toggleAmonia(); //chama função para ocultar o campo alumínio
    toggleEleCarvao(); //chama função para ocultar o campo produção de eletricidade por carvão
    toggleEleGas(); //chama função para ocultar o campo produção de eletricidade por Gás
    toggleElePetroleo(); //chama função para ocultar o campo produção de eletricidade por petróleo
})

function toggleArPequeno(){
    const checkArPequeno = document.getElementById('checkArPequeno');
    const txarP = document.getElementById('txarP');
    const arP =document.getElementById('arP');

    if (checkArPequeno.checked) {
        txarP.style.display = 'block';
        arP.style.display = 'block';
        qtarP.style.display = 'block';
    } else{
        txarP.style.display = 'none';
        arP.style.display = 'none';
        qtarP.style.display = 'none';
    }
}

function toggleArMedio(){
    const checkArMedio = document.getElementById('checkArMedio');
    const txarM = document.getElementById('txarM');
    const arM =document.getElementById('arM');

    if (checkArMedio.checked) {
        txarM.style.display = 'block';
        arM.style.display = 'block';
        qtarM.style.display = 'block';
    } else{
        txarM.style.display = 'none';
        arM.style.display = 'none';
        qtarM.style.display = 'none';
    }
}

function toggleArGrand(){
    const checkArGrande = document.getElementById('checkArGrande');
    const txarG = document.getElementById('txarG');
    const arG =document.getElementById('arG');

    if (checkArGrande.checked) {
        txarG.style.display = 'block';
        arG.style.display = 'block';
        qtarg.style.display = 'block';
    } else{
        txarG.style.display = 'none';
        arG.style.display = 'none';
        qtarg.style.display = 'none';
    }
}

function toggleArIndustrial(){
    const checkArIndustrial = document.getElementById('checkArIndustrial');
    const txarI = document.getElementById('txarI');
    const arI =document.getElementById('arI');

    if (checkArIndustrial.checked) {
        txarI.style.display = 'block';
        arI.style.display = 'block';
        qtarI.style.display = 'block';
    } else{
        txarI.style.display = 'none';
        arI.style.display = 'none';
        qtarI.style.display = 'none';
    }
}
document.addEventListener('DOMContentLoaded',function () {
    toggleArPequeno();
    toggleArMedio();
    toggleArGrand();
    toggleArIndustrial()
})

function toggleSolidos(){
    const checkSolidos = document.getElementById('checkSolidos');
    const txRsSolidos = document.getElementById('txRsSolidos');
    const RsSolidos =document.getElementById('RsSolidos');

    if (checkSolidos.checked) {
        txRsSolidos.style.display = 'block';
        RsSolidos.style.display = 'block';
    } else{
        txRsSolidos.style.display = 'none';
        RsSolidos.style.display = 'none';
    }
}

function toggleOrganicos(){
    const checkOrganicos = document.getElementById('checkOrganicos');
    const txRsOrganicos = document.getElementById('txRsOrganicos');
    const RsOrganicos =document.getElementById('RsOrganicos');

    if (checkOrganicos.checked) {
        txRsOrganicos.style.display = 'block';
        RsOrganicos.style.display = 'block';
    } else{
        txRsOrganicos.style.display = 'none';
        RsOrganicos.style.display = 'none';
    }
}

function toggleIndustriais(){
    const checkIndustriais = document.getElementById('checkIndustriais');
    const txRsIndustriais = document.getElementById('txRsIndustriais');
    const RsIndustriais =document.getElementById('RsIndustriais');

    if (checkIndustriais.checked) {
        txRsIndustriais.style.display = 'block';
        RsIndustriais.style.display = 'block';
    } else{
        txRsIndustriais.style.display = 'none';
        RsIndustriais.style.display = 'none';
    }
}

function toggleEletronicos(){
    const checkEletronicos = document.getElementById('checkEletronicos');
    const txRsEletronicos = document.getElementById('txRsEletronicos');
    const RsEletronicos =document.getElementById('RsEletronicos');

    if (checkEletronicos.checked) {
        txRsEletronicos.style.display = 'block';
        RsEletronicos.style.display = 'block';
    } else{
        txRsEletronicos.style.display = 'none';
        RsEletronicos.style.display = 'none';
    }
}
document.addEventListener('DOMContentLoaded',function () {
    toggleSolidos();
    toggleOrganicos();
    toggleIndustriais();
    toggleEletronicos();
})

function toggleAgricola(){
    const checkAgricola = document.getElementById('checkAgricola');
    const txEfAricola = document.getElementById('txEfAricola');
    const EfAgricola =document.getElementById('EfAgricola');

    if (checkAgricola.checked) {
        txEfAricola.style.display = 'block';
        EfAgricola.style.display = 'block';
    } else{
        txEfAricola.style.display = 'none';
        EfAgricola.style.display = 'none';
    }
}

function toggleDomestico(){
    const checkDomestico = document.getElementById('checkDomestico');
    const txEfDomestico = document.getElementById('txEfDomestico');
    const EfDomestico =document.getElementById('EfDomestico');

    if (checkDomestico.checked) {
        txEfDomestico.style.display = 'block';
        EfDomestico.style.display = 'block';
    } else{
        txEfDomestico.style.display = 'none';
        EfDomestico.style.display = 'none';
    }
}

function toggleIndustrial(){
    const checkIndustrical = document.getElementById('checkIndustrical');
    const txEfIndustriais = document.getElementById('txEfIndustriais');
    const EfIndustriais =document.getElementById('EfIndustriais');

    if (checkIndustrical.checked) {
        txEfIndustriais.style.display = 'block';
        EfIndustriais.style.display = 'block';
    } else{
        txEfIndustriais.style.display = 'none';
        EfIndustriais.style.display = 'none';
    }
}
document.addEventListener('DOMContentLoaded',function () {
    toggleAgricola();
    toggleDomestico();
    toggleIndustrial()
})

function OcultaEnergia() {
    const tpFornecimento = document.getElementById('tpFornecimento').value;
    const txEnCarvao = document.getElementById('txEnCarvao');
    const enCarvao = document.getElementById('enCarvao');
    const txEnGasnatural = document.getElementById('txEnGasnatural');
    const enGasnatural = document.getElementById('enGasnatural');
    const txEnPetroleo = document.getElementById('txEnPetroleo');
    const enPetroleo = document.getElementById('enPetroleo');
    const txEnNuclear = document.getElementById('txEnNuclear');
    const enNuclear = document.getElementById('enNuclear');
    const txEnRenovavel = document.getElementById('txEnRenovavel');
    const enRenovavel = document.getElementById('enRenovavel');

    txEnCarvao.style.display = 'none';
    enCarvao.style.display = 'none';
    txEnGasnatural.style.display = 'none';
    enGasnatural.style.display = 'none';
    txEnPetroleo.style.display = 'none';
    enPetroleo.style.display = 'none';
    txEnNuclear.style.display = 'none';
    enNuclear.style.display = 'none';
    txEnRenovavel.style.display = 'none';
    enRenovavel.style.display = 'none';

    if (tpFornecimento === "1") {
        txEnCarvao.style.display = 'block';
        enCarvao.style.display = 'block';
    } else if (tpFornecimento === "2") {
        txEnGasnatural.style.display = 'block';
        enGasnatural.style.display = 'block';
    } else if (tpFornecimento === "3") {
        txEnPetroleo.style.display = 'block';
        enPetroleo.style.display = 'block';
    } else if (tpFornecimento === "4") {
        txEnNuclear.style.display = 'block';
        enNuclear.style.display = 'block';
    } else if (tpFornecimento === "5") {
        txEnRenovavel.style.display = 'block';
        enRenovavel.style.display = 'block';
    }
}

document.addEventListener('DOMContentLoaded', function () {
    OcultaEnergia();
});
