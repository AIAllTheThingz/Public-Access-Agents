export interface ExampleItem {
  readonly id: string;
  readonly displayName: string;
}

export interface ExampleGateway {
  getById(
    id: string,
    options: {
      readonly signal: AbortSignal;
    },
  ): Promise<ExampleItem | undefined>;
}

export type ExampleResult =
  | {
      readonly kind: "success";
      readonly item: ExampleItem;
    }
  | {
      readonly kind: "notFound";
    };

/**
 * Coordinates a focused application use case.
 */
export class ExampleService {
  readonly #gateway: ExampleGateway;

  public constructor(gateway: ExampleGateway) {
    this.#gateway = gateway;
  }

  /**
   * Retrieves one item while preserving cancellation.
   */
  public async getById(
    id: string,
    options: {
      readonly signal: AbortSignal;
    },
  ): Promise<ExampleResult> {
    const normalizedId = id.trim();

    if (normalizedId.length === 0) {
      throw new TypeError("The item identifier cannot be empty.");
    }

    options.signal.throwIfAborted();

    const item = await this.#gateway.getById(normalizedId, {
      signal: options.signal,
    });

    if (item === undefined) {
      return { kind: "notFound" };
    }

    return {
      kind: "success",
      item,
    };
  }
}
