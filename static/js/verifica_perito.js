document.addEventListener('DOMContentLoaded', function () {
    const cpfInput = document.getElementById('cpf_login'); 
    const labelUnidade = document.getElementById('label-unidade');
    const selectUnidade = document.getElementById('select-unidade');

    if (!cpfInput) {
        console.warn('Campo CPF não encontrado!');
        return;
    }

    cpfInput.addEventListener('blur', function () {
        const cpf = cpfInput.value.trim();
        if (cpf.length < 11) {
            labelUnidade.style.display = 'none';
            selectUnidade.style.display = 'none';
            return;
        }

        fetch(`/verificar_perito/?cpf=${cpf}`)
            .then(response => response.json())
            .then(data => {
                if (data.is_perito) {
                    labelUnidade.style.display = 'block';
                    selectUnidade.style.display = 'block';
                } else {
                    labelUnidade.style.display = 'none';
                    selectUnidade.style.display = 'none';
                }
            })
            .catch(error => console.error('Erro ao verificar perito:', error));
    });
});
