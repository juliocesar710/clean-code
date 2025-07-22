import { describe, it, expect } from 'vitest';
import { calculateAverage } from '../src/services/calculateAverage.js';

describe('calculateAverage', () => {
  it('should calculate the average correctly', () => {
    expect(calculateAverage([10, 8, 6])).toBe(8);
  });

  it('should return NaN when array is empty', () => {
    expect(calculateAverage([])).toBeNaN();
  });
});
