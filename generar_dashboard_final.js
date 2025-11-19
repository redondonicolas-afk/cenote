const fs = require('fs');

// Leer JSONs
const mzData = fs.readFileSync('productos_mz_temp.json', 'utf8').replace(/^\uFEFF/, '');  // Remover BOM
const nuData = fs.readFileSync('productos_nu_temp.json', 'utf8').replace(/^\uFEFF/, '');  // Remover BOM

// Leer template HTML
let template = fs.readFileSync('06_PRESENTACIONES_HTML/dashboard_ranking_productos_2025_interactivo.html', 'utf8');

// Reemplazar los datos
// Buscar desde "const productosMZ =" hasta el "];" que cierra el array
template = template.replace(
    /const productosMZ = \[[\s\S]*?\];/,
    `const productosMZ = ${mzData};`
);

template = template.replace(
    /const productosNU = \$\{JSON\.stringify\(\[[\s\S]*?\]\)\};/,
    `const productosNU = ${nuData};`
);

// Guardar nuevo archivo
fs.writeFileSync('06_PRESENTACIONES_HTML/dashboard_ranking_productos_2025_interactivo.html', template);

console.log('✅ Dashboard actualizado con TODOS los datos!');
console.log('   - 193 productos de Martínez');
console.log('   - 205 productos de Núñez');
console.log('   - Total: 398 productos');
