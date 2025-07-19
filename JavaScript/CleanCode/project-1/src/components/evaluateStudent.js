import { calculateAverage } from '../services/calculateAverage.js';
import { checkApproval } from '../services/checkApproval.js';

export function evaluateStudent(student) {
  const average = calculateAverage(student.grades);
  const status = checkApproval(average) ? 'aprovado' : 'reprovado';

  console.log(`${student.name} foi ${status} com média ${average.toFixed(2)}`);
}
