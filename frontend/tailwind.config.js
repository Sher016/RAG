/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    fontFamily: {
      display: ['"Noto Serif"', 'serif'],
      body: ['Inter', 'sans-serif'],
      times: ['"Times New Roman"', 'Times', 'serif'],
    },
    extend: {
      fontSize: {
        'display-lg': ['3.5rem', { letterSpacing: '-0.02em', lineHeight: '1.1' }],
        'body-md': ['1rem', { lineHeight: '1.5' }],
        'label-sm': ['0.75rem', { lineHeight: '1.2' }],
      }
    },
  },
  plugins: [],
};
