import * as THREE from 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.module.js';

const scene = new THREE.Scene();
// fov é em graus 65, mais amplo, maior o grau mais perto
// window.innerWidth / window.innerHeight: É a relação de aspecto da câmera,
//  definida pela largura e altura da janela. 
// Isso assegura que os objetos não fiquem distorcidos independentemente do tamanho da tela.

//0.1 e 1000: São os planos de corte próximos e distantes (near e far planes). 
// Eles definem os limites da profundidade visível. 
// Objetos mais próximos que 0.1 ou mais distantes que 1000 não serão renderizados.
const camera = new THREE.PerspectiveCamera(65, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight); // renderiza a tela de acordo com o tamamnho da janela do navegador
renderer.setClearColor(0x000000, 1); // Fundo preto
document.body.appendChild(renderer.domElement);

// Posiciona o canvas atrás de todo o conteúdo
renderer.domElement.style.position = 'absolute';
renderer.domElement.style.top = '0';
renderer.domElement.style.left = '0';
renderer.domElement.style.zIndex = '-1'; // Coloca o canvas atrás do conteúdo da página

// Criação das partículas
const particleCount = 6000; // Número de partículas
const particles = new THREE.BufferGeometry();
const positions = [];
const colors = [];

// Cores das partículas (roxa, azul e rosa)
const colorRoxa = new THREE.Color('#891ac5');
const colorAzul = new THREE.Color('#3c3ce5');
const colorRosa = new THREE.Color('#FF1493');

// Distribuição aleatória das partículas e atribuição de cores
for (let i = 0; i < particleCount; i++) {
    const x = (Math.random() - 0.5) * 2 * window.innerWidth; // Aleatório no eixo X
    const y = (Math.random() - 0.5) * 2 * window.innerHeight; // Aleatório no eixo Y
    const z = (Math.random() - 0.5) * 2000; // Aleatório no eixo Z
    positions.push(x, y, z);

    // Atribuindo cores aleatórias entre as três opções
    const color = Math.random() > 0.66 ? colorRoxa : (Math.random() > 0.5 ? colorAzul : colorRosa);
    colors.push(color.r, color.g, color.b);
}

particles.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
particles.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));

// Material das partículas
const particleMaterial = new THREE.PointsMaterial({
    size: 1.1,          // Tamanho das partículas
    vertexColors: true, // Usando cores definidas para cada partícula
    transparent: true,
    opacity: 1,       // Opacidade das partículas
});

// Criação e adição das partículas na cena
const particleSystem = new THREE.Points(particles, particleMaterial);
scene.add(particleSystem);

// Configuração da câmera
camera.position.z = 1000;

// Ajustar o tamanho da tela caso o usuário redimensione a janela
window.addEventListener('resize', () => {
    renderer.setSize(window.innerWidth, window.innerHeight);
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
});

// Animação
function animate() {
    requestAnimationFrame(animate);

    // Opcional: Rotação do sistema de partículas
    particleSystem.rotation.y += 0.0001;

    renderer.render(scene, camera);
}
animate();
