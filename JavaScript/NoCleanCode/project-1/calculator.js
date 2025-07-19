function calculator(n1, n2, n3, n) {
    let m = (n1 + n2 + n3) / 3;
    if (m >= 7) {
        console.log(n + ' foi aprovado com média ' + m);
    } else {
        console.log(n + ' foi reprovado com média ' + m);
    }
}

calculator(5, 7, 9, 'Carlos');
calculator(8, 6, 9, 'Julia');
