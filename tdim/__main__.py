"""Main application code."""

##############################################################################
# Textual imports.
from textual.app        import App, ComposeResult
from textual.binding    import Binding
from textual.containers import Container
from textual.widgets    import Label

##############################################################################
class Dimensions( App[ None ] ):
    """Application to show the dimensions of the terminal."""

    CSS = """
    Screen {
        align: center middle;
    }

    Container {
        align: center middle;
        width: 1fr;
        height: 1fr;
    }

    Container.bordered {
        border: thick white;
    }
    """
    """The stylesheet for the application."""

    BINDINGS = [
        Binding( "b", "border", "Show/hide the border" ),
        Binding( "escape", "quit", "Quit the application" ),
        Binding( "0", "clear", "Clear the target ratio" ),
        Binding( "1", "ratio( 16, 9 )", "16x9" ),
        Binding( "2", "ratio( 4, 3 )", "4x3" ),
        Binding( "3", "ratio( 2, 1 )", "2x1" ),
        Binding( "4", "ratio( 1, 1 )", "1x1" ),
    ]
    """Bindings for the application."""

    def compose( self ) -> ComposeResult:
        """Compose the child widgets."""
        with Container():
            yield Label()

    def on_resize( self ) -> None:
        """Handle the terminal being resized."""
        self.query_one(Label).update(
            f"{self.console.width} x {self.console.height}"
        )

    def action_border( self ) -> None:
        """Toggle a display of a border."""
        self.query_one( Container ).toggle_class( "bordered" )

    def action_clear( self ) -> None:
        display = self.query_one( Container )
        display.styles.width  = "1fr"
        display.styles.height = "1fr"
        display.border_title  = ""

    def action_ratio( self, width: int, height: int ) -> None:
        """Set a target aspect ratio.

        Args:
            width: The target width.
            height: The target height.
        """
        display = self.query_one( Container )
        display.set_class( True, "bordered" )
        display.styles.width  = self.console.width
        display.styles.height = ( ( self.console.width / 2 ) / width ) * height
        display.border_title  = f"Aiming for {width} x {height}"

##############################################################################
def run() -> None:
    """Run the application."""
    Dimensions().run()

##############################################################################
if __name__ == "__main__":
    run()

### __main__.py ends here
