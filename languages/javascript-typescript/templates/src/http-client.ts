export interface HttpJsonClientOptions {
  readonly baseUrl: URL;
  readonly timeoutMs: number;
}

/**
 * Provides bounded JSON retrieval through the Node.js fetch implementation.
 */
export class HttpJsonClient {
  readonly #baseUrl: URL;
  readonly #timeoutMs: number;

  public constructor(options: HttpJsonClientOptions) {
    if (options.baseUrl.protocol !== "https:") {
      throw new TypeError("The HTTP client base URL must use HTTPS.");
    }

    if (!Number.isInteger(options.timeoutMs) || options.timeoutMs <= 0) {
      throw new TypeError("The HTTP client timeout must be a positive integer.");
    }

    this.#baseUrl = new URL(options.baseUrl);
    this.#timeoutMs = options.timeoutMs;
  }

  public async get(
    relativePath: string,
    options: {
      readonly signal?: AbortSignal;
    } = {},
  ): Promise<unknown> {
    const url = new URL(relativePath, this.#baseUrl);

    // AbortSignal.any preserves caller cancellation while also enforcing a
    // client-owned timeout. Neither signal is silently discarded.
    const signal =
      options.signal === undefined
        ? AbortSignal.timeout(this.#timeoutMs)
        : AbortSignal.any([
            options.signal,
            AbortSignal.timeout(this.#timeoutMs),
          ]);

    const response = await fetch(url, {
      method: "GET",
      headers: {
        accept: "application/json",
      },
      redirect: "error",
      signal,
    });

    if (!response.ok) {
      throw new Error(
        `The remote service returned HTTP ${response.status}.`,
      );
    }

    return response.json() as Promise<unknown>;
  }
}
