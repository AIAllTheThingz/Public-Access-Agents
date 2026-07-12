import { afterEach, describe, expect, it } from "vitest";

describe("controlled integration example", () => {
  const resources: Array<() => Promise<void>> = [];

  afterEach(async () => {
    // Clean up resources in reverse order so dependent resources are released
    // before the infrastructure they depend on.
    for (const cleanup of resources.reverse()) {
      await cleanup();
    }

    resources.length = 0;
  });

  it("uses only controlled non-production dependencies", async () => {
    /*
     * Replace this placeholder with a controlled server, container, temporary
     * filesystem, or non-production service.
     *
     * Never use production credentials or production targets.
     */
    expect(true).toBe(true);
  });
});
