extends Sprite

var angular_speed = PI
var speed = 400.0

func _process(delta: float) -> void:
	var direction = 0
	if Input.is_action_pressed("ui_left"):
		direction = -1
	if Input.is_action_pressed("ui_right"):
		direction = 1
	
	rotation += angular_speed * direction * delta
	
	var velocity =Vector2.ZERO
	if Input.is_action_pressed("ui_up"):
		velocity = Vector2.UP
	
	velocity = velocity.rotated(rotation)
	position += velocity * speed * delta
