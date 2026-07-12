using System.Net;
using Microsoft.AspNetCore.Mvc.Testing;

namespace Example.Project.Api.Tests;

public sealed class ExampleEndpointTests :
    IClassFixture<WebApplicationFactory<Program>>
{
    private readonly WebApplicationFactory<Program> _factory;

    public ExampleEndpointTests(
        WebApplicationFactory<Program> factory)
    {
        _factory = factory;
    }

    [Fact]
    public async Task Get_WhenUserIsNotAuthenticated_ReturnsUnauthorized()
    {
        // Arrange
        using HttpClient client = _factory.CreateClient();

        // Act
        using HttpResponseMessage response = await client.GetAsync(
            "/api/examples/example-001",
            TestContext.Current.CancellationToken);

        // Assert
        Assert.Equal(HttpStatusCode.Unauthorized, response.StatusCode);
    }

    /*
      Add authenticated test clients and controlled service replacements for
      successful and forbidden scenarios.

      Integration tests must not use production credentials or services.
      Replace external dependencies with controlled containers, fakes, or
      non-production endpoints.
    */
}
