export function calculateAverage(grades) {
  const sum = grades.reduce((acc, grade) => acc + grade, 0);
  return sum / grades.length;
}
