import { describe, expect, it, vi } from "vitest";

import {
  ExampleService,
  type ExampleGateway,
} from "../src/service.js";

describe("ExampleService", () => {
  it("returns success when the gateway returns an item", async () => {
    const controller = new AbortController();

    const gateway: ExampleGateway = {
      getById: vi.fn().mockResolvedValue({
        id: "example-001",
        displayName: "Example",
      }),
    };

    const service = new ExampleService(gateway);

    const result = await service.getById("example-001", {
      signal: controller.signal,
    });

    expect(result).toEqual({
      kind: "success",
      item: {
        id: "example-001",
        displayName: "Example",
      },
    });
  });

  it("rejects an empty identifier before calling the gateway", async () => {
    const controller = new AbortController();

    const gateway: ExampleGateway = {
      getById: vi.fn(),
    };

    const service = new ExampleService(gateway);

    await expect(
      service.getById(" ", {
        signal: controller.signal,
      }),
    ).rejects.toThrow(TypeError);

    expect(gateway.getById).not.toHaveBeenCalled();
  });

  it("preserves caller cancellation", async () => {
    const controller = new AbortController();
    controller.abort();

    const gateway: ExampleGateway = {
      getById: vi.fn(),
    };

    const service = new ExampleService(gateway);

    await expect(
      service.getById("example-001", {
        signal: controller.signal,
      }),
    ).rejects.toMatchObject({
      name: "AbortError",
    });

    expect(gateway.getById).not.toHaveBeenCalled();
  });
});
