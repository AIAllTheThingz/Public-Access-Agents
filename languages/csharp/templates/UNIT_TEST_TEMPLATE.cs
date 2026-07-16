using System;
using System.Threading;
using System.Threading.Tasks;
using Example.CSharp;
using Xunit;

namespace Example.CSharp.Tests;

/// <summary>
/// Demonstrates behavior-focused tests for the async service template.
/// </summary>
public sealed class SampleServiceTests
{
    [Fact]
    public async Task ExecuteAsync_WhenValueExists_ReturnsFoundResult()
    {
        var client = new StubSampleClient("resolved-value");
        var service = new SampleService(client);

        SampleResult result = await service.ExecuteAsync("sample-id", CancellationToken.None);

        Assert.True(result.IsFound);
        Assert.Equal("sample-id", result.Identifier);
        Assert.Equal("resolved-value", result.Value);
    }

    [Fact]
    public async Task ExecuteAsync_WhenCancellationRequested_PropagatesCancellation()
    {
        var client = new StubSampleClient("unused");
        var service = new SampleService(client);
        using var cancellation = new CancellationTokenSource();
        cancellation.Cancel();

        await Assert.ThrowsAsync<OperationCanceledException>(
            () => service.ExecuteAsync("sample-id", cancellation.Token));

        Assert.Equal(0, client.CallCount);
    }

    private sealed class StubSampleClient(string? value) : ISampleClient
    {
        public int CallCount { get; private set; }

        public Task<string?> GetValueAsync(
            string identifier,
            CancellationToken cancellationToken)
        {
            ArgumentException.ThrowIfNullOrWhiteSpace(identifier);
            cancellationToken.ThrowIfCancellationRequested();
            CallCount++;
            return Task.FromResult(value);
        }
    }
}
