import { describe, it, expect } from "vitest";
import { checkApproval } from "../src/services/checkApproval.js";

describe("checkApproval", () => {
  it("should return true for average >= 7", () => {
    expect(checkApproval(7)).toBe(true);
    expect(checkApproval(8)).toBe(true);
    expect(checkApproval(10)).toBe(true);
  });

  it("should return false for average < 7", () => {
    expect(checkApproval(6)).toBe(false);
    expect(checkApproval(5.5)).toBe(false);
    expect(checkApproval(0)).toBe(false);
  });
});