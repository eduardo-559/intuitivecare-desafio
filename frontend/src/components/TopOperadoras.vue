<template>
    <div class="top-operadoras">
      <h2>Top 10 Operadoras por Saldo Final</h2>
      <table>
        <thead>
          <tr>
            <th>Registro ANS</th>
            <th>Total em R$</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="op in operadoras" :key="op.reg_ans">
            <td>{{ op.reg_ans }}</td>
            <td>R$ {{ format(op.total_saldo) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        operadoras: []
      };
    },
    methods: {
      format(valor) {
        return Number(valor).toLocaleString("pt-BR", {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        });
      }
    },
    mounted() {
      fetch("http://localhost:5000/api/top-operadoras")
        .then(res => res.json())
        .then(data => {
          this.operadoras = data;
        });
    }
  };
  </script>
  
  <style>
  .top-operadoras {
    font-family: Arial, sans-serif;
    margin: 20px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
  }
  th, td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: left;
  }
  thead {
    background-color: #f4f4f4;
  }
  </style>
  