/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.html"],
  theme: {
    extend: {
      colors:{
        Gray: '#f0f5f8',
        Orange: '#ff8b18',
        Blue:'#1b3faa',
        BlueGray:'#d3dfea',
        Whitish:'#f4f5f7',
        DarkBlue:'#19389f',
        Green: '#95cb00',
        Yellow:'#ffc330',
        Dark:'#0f0f1a',
        WhitishGray:'#e2e2e2',
        Red:'#d72428',
        Transparent:'rgba(128, 128, 128, 0.507)'
      }
    },
  },
  plugins: [],
}
