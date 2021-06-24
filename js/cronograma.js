class Pedidos {
    leer (lsPedidos){
        this.lista = lsPedidos;
    }
    crear (nuevoPedido){
        this.lista.push(nuevoPedido)
    }
    getById (id){
        return this.lista.find( el => el.id === id);
    }
    editar (current) {
        this.lista = this.lista.map( el => el.id === current.id ? current : el)
    }
    borrar (id){
        this.lista = this.lista.filter( el => el.id !== id)
    }
}

let isEditing = false;
let currentPedido = null;
const tablaPedidos = $('#listaPedidos');
const inputCliente = $('#inputCliente');
const inputFechaDeRecibo = $('#inputFechaDeRecibo');
const inputTipoPedido = $('#inputTipoPedido');
const inputFechaLimEntrega = $('#inputFechaLimEntrega');
const inputLugarEntrega = $('#inputLugarEntrega');
const inputMedioEntrega = $('#inputMedioEntrega');

//TODO: leer pedidos
let listaPedidos = [
    {
        id: 0,
        Cliente: "Estefanía Marín",
        FechaDeRecibo: "12/03/2021",
        TipoDepedido: "Colección",
        FechaLimiteDeEntrega: "19/08/2021",
        LugarDeEntrega: "Cra 59 # 70-349",
        MedioDeEntrega: "Correo",
    },
    {
        id: 1,
        Cliente: "Daniel Silva",
        FechaDeRecibo: "12/03/2021",
        TipoDepedido: "Colección",
        FechaLimiteDeEntrega: "19/08/2021",
        LugarDeEntrega: "Cra 59 # 70-349",
        MedioDeEntrega: "Correo",
    },
    {
        id: 2,
        Cliente: "Rufis Molina",
        FechaDeRecibo: "12/03/2021",
        TipoDepedido: "Colección",
        FechaLimiteDeEntrega: "19/08/2021",
        LugarDeEntrega: "Cra 59 # 70-349",
        MedioDeEntrega: "Correo",
    }
];
const pedidos = new Pedidos();
pedidos.leer(listaPedidos);

const deleteRow = (id) => {
    pedidos.borrar(id);
    renderList();
}

const editRow = (id) => {
    isEditing = true;
    currentPedido = id;
    const current = pedidos.getById(id);
    inputCliente.val(current.Cliente);
    inputFechaDeRecibo.val(current.FechaDeRecibo);
    inputTipoPedido.val(current.TipoDepedido);
    inputFechaLimEntrega.val(current.FechaLimiteDeEntrega);
    inputLugarEntrega.val(current.LugarDeEntrega);
    inputMedioEntrega.val(current.MedioDeEntrega);
}

const addRow = (el) => {
    tablaPedidos.find('tbody').append(`
        <tr>
            <td>${el.id}</td>
            <td>${el.Cliente}</td>
            <td>${el.FechaDeRecibo}</td>
            <td>${el.TipoDepedido}</td>
            <td>${el.FechaLimiteDeEntrega}</td>
            <td>${el.LugarDeEntrega}</td>
            <td>${el.MedioDeEntrega}</td>
            <td>
                <input
                type="button" 
                value="✏️" 
                class="btn btn-success float-right"
                onclick="editRow(${el.id})"
                >
            </td>
            <td>
                <input
                    style="background-color: rgb(255, 51, 51 ) !important;"
                    type="button"
                    value="🗑️"
                    class="btn btn-success float-right"
                    onclick="deleteRow(${el.id})"
                />
            </td>
        </tr>
    `)
}

renderList = () => {
    tablaPedidos.find('tbody').empty();
    pedidos.lista.forEach((el) => {
        addRow(el);
    })
}

const manejarPedido = () => {
    const templatePedido = {
        id: Date.now(),
        Cliente: inputCliente.val(),
        FechaDeRecibo: inputFechaDeRecibo.val(),
        TipoDepedido: inputTipoPedido.val(),
        FechaLimiteDeEntrega: inputFechaLimEntrega.val(),
        LugarDeEntrega: inputLugarEntrega.val(),
        MedioDeEntrega: inputMedioEntrega.val(),
    }
    pedidos.crear(templatePedido);
    inputCliente.val('');
    inputFechaDeRecibo.val('');
    inputTipoPedido.val('');
    inputFechaLimEntrega.val('');
    inputLugarEntrega.val('');
    inputMedioEntrega.val('');
    renderList();
}

const actualizarPedido = () => {
    const templatePedido = {
        id: currentPedido,
        Cliente: inputCliente.val(),
        FechaDeRecibo: inputFechaDeRecibo.val(),
        TipoDepedido: inputTipoPedido.val(),
        FechaLimiteDeEntrega: inputFechaLimEntrega.val(),
        LugarDeEntrega: inputLugarEntrega.val(),
        MedioDeEntrega: inputMedioEntrega.val(),
    };
    pedidos.editar(templatePedido);
    inputCliente.val('');
    inputFechaDeRecibo.val('');
    inputTipoPedido.val('');
    inputFechaLimEntrega.val('');
    inputLugarEntrega.val('');
    inputMedioEntrega.val('');
    renderList();
}

console.log(pedidos.lista)

$(document).ready(() => {
    renderList();
});