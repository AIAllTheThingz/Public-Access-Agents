namespace Example.Project.Tests;

public sealed class ExampleComponentTests
{
    [Fact]
    public void Create_WhenIdentifierIsValid_ReturnsExpectedResult()
    {
        // Arrange
        DateTimeOffset expectedTime = new(
            2026,
            1,
            15,
            12,
            0,
            0,
            TimeSpan.Zero);

        FakeTimeProvider timeProvider = new(expectedTime);
        ExampleComponent component = new(timeProvider);

        // Act
        ExampleResult result = component.Create("example-001");

        // Assert
        Assert.Equal("example-001", result.Identifier);
        Assert.Equal(expectedTime, result.CreatedAtUtc);
    }

    [Theory]
    [InlineData("")]
    [InlineData(" ")]
    public void Create_WhenIdentifierIsEmpty_ThrowsArgumentException(
        string identifier)
    {
        // Arrange
        ExampleComponent component = new(TimeProvider.System);

        // Act
        Action action = () => component.Create(identifier);

        // Assert
        ArgumentException exception = Assert.Throws<ArgumentException>(action);
        Assert.Equal("identifier", exception.ParamName);
    }

    private sealed class FakeTimeProvider : TimeProvider
    {
        private readonly DateTimeOffset _utcNow;

        public FakeTimeProvider(DateTimeOffset utcNow)
        {
            _utcNow = utcNow;
        }

        public override DateTimeOffset GetUtcNow() => _utcNow;
    }
}
