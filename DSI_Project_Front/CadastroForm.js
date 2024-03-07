import React, { useState } from 'react';

const CadastroForm = () => {
  const [usuario, setUsuario] = useState({
    nome: '',
    email: '',
    senha: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUsuario({ ...usuario, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Substitua a URL abaixo pela URL real da sua API de cadastro
      const response = await fetch('npm', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(usuario),
      });

      if (response.ok) {
        console.log('Cadastro bem-sucedido!');
        // Adicione lógica adicional, se necessário
      } else {
        console.error('Erro no cadastro:', response.statusText);
      }
    } catch (error) {
      console.error('Erro ao enviar dados para a API:', error);
    }
  };

  return (
    <div>
      <h2>Cadastro de Usuário</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Nome:
          <input
            type="text"
            name="nome"
            value={usuario.nome}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <label>
          Email:
          <input
            type="email"
            name="email"
            value={usuario.email}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <label>
          Senha:
          <input
            type="password"
            name="senha"
            value={usuario.senha}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <button type="submit">Cadastrar</button>
      </form>
    </div>
  );
};

export default CadastroForm;
